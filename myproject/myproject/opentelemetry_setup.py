# SET UP CONNECTION STRING
from dotenv import load_dotenv
import os
load_dotenv()
APPLICATIONINSIGHTS_CONNECTION_STRING=os.getenv('APPLICATIONINSIGHTS_CONNECTION_STRING')
INSTRUMENTATION_KEY = os.getenv('INSTRUMENTATION_KEY')

# PART 1 : SET UP LOGGING EXPORTER
import logging
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry._logs import set_logger_provider
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from azure.monitor.opentelemetry.exporter import AzureMonitorLogExporter

## creates an AzureMonitorLogExporter instance with the connection string
exporter = AzureMonitorLogExporter(
    connection_string=APPLICATIONINSIGHTS_CONNECTION_STRING
)
## sets up a LoggerProvider and adds a BatchLogRecordProcessor to export logs in batches.
logger_provider = LoggerProvider()
set_logger_provider(logger_provider)
logger_provider.add_log_record_processor(BatchLogRecordProcessor(exporter))

# Attach LoggingHandler to namespaced logger(root logger) and sets the log level to INFO.
handler = LoggingHandler()
logger = logging.getLogger(__name__)
logger.addHandler(handler)

logger.setLevel(logging.INFO)


# PART 2 : SET UP TRACE EXPORTER to send tracing data to Azure Monitor.
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from azure.monitor.opentelemetry.exporter import AzureMonitorTraceExporter

## creates an AzureMonitorTraceExporter instance with the connection string.
trace_exporter = AzureMonitorTraceExporter(
    connection_string=APPLICATIONINSIGHTS_CONNECTION_STRING
)
## sets up a TracerProvider with a Resource that includes attributes for the service name and cloud role.Adds a BatchSpanProcessor to export spans in batches
resource = Resource(attributes={"cloud.role": "DjangoApplication","service.name":"DjangoApplication"})
tracer_provider = TracerProvider(resource=resource)
tracer_provider.add_span_processor(BatchSpanProcessor(trace_exporter))
## sets the TracerProvider as the global tracer provider and gets a tracer instance.
trace.set_tracer_provider(tracer_provider)
tracer = trace.get_tracer(__name__)


# PART 3 : Instrument Django and Request for automatic HTTP logging and tracing data
from opentelemetry.instrumentation.django import DjangoInstrumentor
DjangoInstrumentor().instrument()   # uses DjangoInstrumentor to instrument the Django application
from opentelemetry.instrumentation.requests import RequestsInstrumentor
RequestsInstrumentor().instrument()  # uses RequestsInstrumentor to instrument the requests library




# PART 4 : SET UP METRICS EXPORTER to send metrics data to Azure Monitor
from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from azure.monitor.opentelemetry.exporter import AzureMonitorMetricExporter

## Create an instance of the AzureMonitorMetricExporter class, passing in the connection string for the Azure Monitor instance to send metrics data to Azure Monitor.
metric_exporter = AzureMonitorMetricExporter(
    connection_string=APPLICATIONINSIGHTS_CONNECTION_STRING
)
## Create a PeriodicExportingMetricReader instance, which is responsible for reading metrics data from the meter and exporting it to the Azure Monitor exporter at regular intervals
frequency_millis = 60000    # the metrics data will be exported every 60 seconds (60,000 milliseconds)
reader = PeriodicExportingMetricReader(exporter=metric_exporter, export_interval_millis=frequency_millis)
## Set up a MeterProvider instance, passing in the PeriodicExportingMetricReader instance as a metric reader
metrics.set_meter_provider(MeterProvider(metric_readers=[reader]))
## Create a meter instance and a counter metric instrument:
meter = metrics.get_meter_provider().get_meter("satisfaction_metrics")

# Create metric instruments
prediction_counter_per_minute = meter.create_counter("prediction_counter_per_minute")   # This counter can be used to track the number of predictions made per minute.