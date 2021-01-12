## Goals 

Goals for the Observability Framework: 
* Standardizing log correlation with traces and metrics 
* Supports distributed context propagation for logs
* Unification of source attribution of logs, traces and metrics 

Goals for observing our solution: 
* Troubleshooting
* Profiling sections of the code and e2e flow 
* Auditing  


## Standards

Telemetry data has the following components: 
* `Name` is a short event identifier used for filtering and grouping purposes 
    * ProcessStarted
    * ProcessOngoing
    * ProcessEnded 
* Severity Fields such as `SeverityText` and `SeverityNumber`
* `Resource` context which is the source of telemetry data
* `Timestamp`
* `Body` which is the message/data
* Execution context where `TraceId` and `SpanId` will also be captured in logs where possible to enable correlation across logs, traces and metrics signals
* `Attributes`

Log records abides by [OpenTelemetry log data model](https://github.com/open-telemetry/opentelemetry-specification/blob/master/specification/logs/data-model.md) and the following applies: 
* Message/data in logs should include: 
    * params are added in message to recreate error if needed
    * unique identifiers is prepended to log message where possible and is related to the id of the item that triggered the e2e flow, for example, an uploaded dicom image. 
    * success is captured in message by appending `"ProcessEnded with success"`
    * messages are machine parseable 
* Application native logging libraries/OpenTelemetry SDKs will be modified/adopted to emit logs according to [OpenTelemetry log data model](https://github.com/open-telemetry/opentelemetry-specification/blob/master/specification/logs/data-model.md)

## Framework 

Centrally collect Traces, Metrics, and Logs (Exceptions, Error,  Warning, Info) by auto and manual instrumentation of solution that generates: 
* App Logs 
* System Logs 
* Traces 
* App metrics 
* Infrastructure Metrics 

Enrichment of Data is based on: 
* Infrastructure attributes
* Custom messages/data  

![framework](./img/unified-collection.png)

## Additional Reading 

[OpenTelemetry Logging Overview](https://github.com/open-telemetry/opentelemetry-specification/blob/master/specification/logs/overview.md)

[OpenTelemetry Log Data Model](https://github.com/open-telemetry/opentelemetry-specification/blob/master/specification/logs/data-model.md)