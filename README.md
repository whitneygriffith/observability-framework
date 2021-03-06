# Introduction 

This captures our observability framework based on the [opentelemetry](https://opentelemetry.io/) standard that can be leveraged in future engagements.  

Additional Observability Philosophy is captured [here](./docs/OBSERVABILITY.md)


## Telemetry Data 

Telemetry data is catured from: 
* Service to Service interactions 
* External network requests to and from services 
* Within a service (function calls, requests ...) 

Telemetry data is of the following formats: 
* Traces 
* Logs 
* Metrics 
## Observability Layers 

1. [Instrumentation of Application Layer](#Instrumentation-of-Application-Layer)  
2. [Instrumentation of Platform Layer](#Instrumentation-of-Platform-Layer)
3. [Collection of all telemetry](#Collection-of-all-telemetry) 
4. [Exporting of all telemetry](#Exporting-of-all-telemetry) 
5. [Display of telemetry data](#Display-of-telemetry-data) 
6. [Response to telemetry data](#Response-to-telemetry-data) 

### Instrumentation of Application Layer

Code level instrumentation to generate telemetry data 

[Python Instrumentation](./code/python_app)
### Instrumentation of Platform Layer

Service Mesh and other utilities that are able to monitor and pull data from infrastructure, network behavior and interactions between services. 

Examples of the platform can be kubernetes cluster. 

[LinkerD](./code/linkerd)

[Unified Logging Layer](./code/logging)

### Collection of all telemetry

Centralized collection of all telemetry data for a given solution.

[opentelemetry collector](./otel_collector)

### Exporting of all telemetry 

Adaptable, flexible, extensible way to export varying types of telemetry data to different backends 

[OSS Observability Backends](./otel_exporters)

### Display of telemetry data 

Ability to query and view data via graphs and dashboards. 
### Response to telemetry data

**Alerts**

Signify that a human needs to take action immediately in response to something that is either happening or about to happen, in order to improve the situation.

**Tickets**

Signify that a human needs to take action, but not immediately. The system cannot automatically handle the situation, but if a human takes action in a few days, no damage will result.

**Logging**

No one needs to look at this information, but it is recorded for diagnostic or forensic purposes. The expectation is that no one reads logs unless something else prompts them to do so.

# What's next for this framework?

* [Display of telemetry data for traces and metrics](#Display-of-telemetry-data ) 