import logging
from contextlib import contextmanager
from typing import Any, Callable, Dict, Iterator, Union
from importlib import import_module
import time
import json

from opentelemetry import trace as trace_api
from opentelemetry.instrumentation.instrumentor import BaseInstrumentor
from opentelemetry.trace import INVALID_SPAN
from wrapt import wrap_function_wrapper

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

_MODULE = import_module("outerop")

class OuteropInstrumentor(BaseInstrumentor):
    def instrumentation_dependencies(self):
        return []

    def _instrument(self, **kwargs: Any) -> None:
        tracer_provider = kwargs.get("tracer_provider")
        tracer = trace_api.get_tracer(__name__, tracer_provider=tracer_provider)

        wrap_function_wrapper(
            module=_MODULE,
            name="Outerop.chat",
            wrapper=_OuteropRequest(tracer),
        )

    def _uninstrument(self, **kwargs: Any) -> None:
        unwrap(_MODULE.Outerop, "chat")

class _OuteropRequest:
    def __init__(self, tracer):
        self._tracer = tracer

    @contextmanager
    def _start_as_current_span(self, span_name: str) -> Iterator:
        try:
            span = self._tracer.start_span(name=span_name)
        except Exception:
            logger.exception("Failed to start span")
            span = INVALID_SPAN
        with trace_api.use_span(
            span,
            end_on_exit=False,
            record_exception=False,
            set_status_on_exception=False,
        ) as span:
            yield span

    def __call__(
    self,
    wrapped: Callable,
    instance: Any,
    args: Any,
    kwargs: Any,
):
        prompt_uuid = kwargs.get("prompt_uuid")
        environment = kwargs.get("environment")
        version = kwargs.get("version")
        variables = kwargs.get("variables")

        span_name = f"Outerop.chat ({prompt_uuid})"

        with self._start_as_current_span(span_name) as span:
            start_time = time.perf_counter()
            try:
                result = wrapped(*args, **kwargs)
            except Exception as exception:
                span.record_exception(exception)
                status = trace_api.Status(
                    status_code=trace_api.StatusCode.ERROR,
                    description=f"{type(exception).__name__}: {exception}",
                )
                span.set_status(status)
                raise
            end_time = time.perf_counter()
            latency_ms = round((end_time - start_time) * 1000)

            prompt = instance.get_prompt(prompt_uuid, environment, version) # Return prompt as result to avoid duplicate requests
            messages_without_id = [
                {k: v for k, v in message.items() if k != "id"}
                for message in _MODULE.replace_variables_in_prompts(prompt["messages"], variables)
            ]

            span.set_attribute("version", prompt["version"])
            span.set_attribute("prompt_uuid", prompt_uuid)
            span.set_attribute("variables", variables)
            span.set_attribute("team_prompt_id", prompt["team_prompt_id"])
            span.set_attribute("environment", prompt["environment"])
            span.set_attribute("prompt_environment_id", prompt["id"])
            span.set_attribute("input", json.dumps(messages_without_id))
            span.set_attribute("output", result.choices[0].message.content)
            span.set_attribute("latency_ms", latency_ms)
            span.set_attribute("output_tokens", result.usage.completion_tokens)
            span.set_attribute("input_tokens", result.usage.prompt_tokens)
            span.set_attribute("model_config_id", prompt["model_config_id"])

            span.set_status(trace_api.Status(status_code=trace_api.StatusCode.OK))
            span.end()

        return result