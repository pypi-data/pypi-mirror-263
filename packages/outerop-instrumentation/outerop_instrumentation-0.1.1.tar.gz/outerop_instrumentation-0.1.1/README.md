# OuteropInstrumentor

The OuteropInstrumentor is a powerful tool designed to integrate Outerop services with OpenTelemetry, providing observability and tracing capabilities for applications using Outerop. This package allows developers to easily instrument their code, enabling detailed insights into the performance and behavior of their Outerop interactions.

## Installation

To install the OuteropInstrumentor, you need to have Python installed on your machine. Then, you can install the package using pip:

```bash
pip install outerop-instrumentation
```

Ensure you also have outerop installed:

```bash
pip install outerop 
```
## Quick Start
To get started with OuteropInstrumentor, follow the steps below to instrument your application:

Configure OpenTelemetry Tracer Provider:
```python

from opentelemetry import trace as trace_api
from outerop import Outerop
from outerop_instrumentation import OuteropInstrumentor
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk import trace as trace_sdk

# Endpoint for the OTLP exporter
endpoint = "http://localhost:4318/v1/traces"

# Resource attributes
resource = Resource.create({"service.name": "outerop-service"})

# Tracer provider setup
tracer_provider = trace_sdk.TracerProvider(resource=resource)
tracer_provider.add_span_processor(SimpleSpanProcessor(ConsoleSpanExporter()))
tracer_provider.add_span_processor(SimpleSpanProcessor(OTLPSpanExporter(endpoint)))
trace_api.set_tracer_provider(tracer_provider)

# Instrument Outerop
OuteropInstrumentor().instrument()

outerop = Outerop(outerop_api_key="your_api_key", options={
    "openaiApiKey": "your_openai_api_key"
})

result = outerop.chat(
    prompt_uuid="<UUID>",
    environment="<environment>",
    version="<Version>",
    variables={"variable": "example"}
)
```

## Usage
After following the quick start guide, your application will be instrumented to provide tracing data to the specified backend (e.g., console, OTLP exporter). You can customize the tracing setup by adjusting the OpenTelemetry and Outerop configurations according to your needs.

For more advanced usage and configurations, refer to the OpenTelemetry and Outerop documentation.

## Support
If you encounter any issues or have questions about using the OuteropInstrumentor, please file an issue on our GitHub repository.

## Contributing
We welcome contributions! If you would like to contribute to the project, please read our CONTRIBUTING.md file for guidelines.