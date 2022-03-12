# Apache_Custom_Exporter

* Exporter provides a flask api endpoint which displays various stats of apache server status.
* These stats can be used by prometheus for monitoring.

Example snippet of stats


```console
# HELP python_gc_objects_collected_total Objects collected during gc
# TYPE python_gc_objects_collected_total counter
python_gc_objects_collected_total{generation="0"} 187.0
python_gc_objects_collected_total{generation="1"} 269.0
python_gc_objects_collected_total{generation="2"} 0.0
# HELP python_gc_objects_uncollectable_total Uncollectable object found during GC
# TYPE python_gc_objects_uncollectable_total counter
python_gc_objects_uncollectable_total{generation="0"} 0.0
python_gc_objects_uncollectable_total{generation="1"} 0.0
python_gc_objects_uncollectable_total{generation="2"} 0.0
# HELP python_gc_collections_total Number of times this generation was collected
# TYPE python_gc_collections_total counter
python_gc_collections_total{generation="0"} 62.0
python_gc_collections_total{generation="1"} 5.0
python_gc_collections_total{generation="2"} 0.0
# HELP python_info Python platform information
# TYPE python_info gauge
python_info{implementation="CPython",major="3",minor="6",patchlevel="8",version="3.6.8"} 1.0
# HELP process_virtual_memory_bytes Virtual memory size in bytes.
# TYPE process_virtual_memory_bytes gauge
process_virtual_memory_bytes 2.55721472e+08
# HELP process_resident_memory_bytes Resident memory size in bytes.
# TYPE process_resident_memory_bytes gauge
process_resident_memory_bytes 2.547712e+07
# HELP process_start_time_seconds Start time of the process since unix epoch in seconds.
# TYPE process_start_time_seconds gauge
process_start_time_seconds 1.64706875655e+09
# HELP process_cpu_seconds_total Total user and system CPU time spent in seconds.
# TYPE process_cpu_seconds_total counter
process_cpu_seconds_total 0.33999999999999997
# HELP process_open_fds Number of open file descriptors.
# TYPE process_open_fds gauge
process_open_fds 7.0
# HELP process_max_fds Maximum number of open file descriptors.
# TYPE process_max_fds gauge
process_max_fds 1.048576e+06
# HELP SERVER_STATUS_total Help text
# TYPE SERVER_STATUS_total counter
SERVER_STATUS_total{value="server_load"} 0.0
# HELP SERVER_STATUS_total Help text
# TYPE SERVER_STATUS_total counter
SERVER_STATUS_total{value="server_load_1"} 0.0
# HELP SERVER_STATUS_total Help text
# TYPE SERVER_STATUS_total counter
SERVER_STATUS_total{value="server_load_2"} 0.0
# HELP SERVER_STATUS_total Help text
# TYPE SERVER_STATUS_total counter
SERVER_STATUS_total{value="up_status"} 0.0
# HELP SERVER_STATUS_total Help text
# TYPE SERVER_STATUS_total counter
SERVER_STATUS_total{value="cpu_usage"} 0.0
# HELP SERVER_STATUS_total Help text
# TYPE SERVER_STATUS_total counter
SERVER_STATUS_total{value="access_count"} 0.0
# HELP SERVER_STATUS_total Help text
# TYPE SERVER_STATUS_total counter
SERVER_STATUS_total{value="idle workers"} 0.0
# HELP SERVER_STATUS_total Help text
# TYPE SERVER_STATUS_total counter
SERVER_STATUS_total{value="Server UP Time"} 0.0
# HELP SERVER_STATUS_total Help text
# TYPE SERVER_STATUS_total counter
SERVER_STATUS_total{value="Current workers"} 0.0
# HELP SERVER_STATUS_total Help text
# TYPE SERVER_STATUS_total counter
SERVER_STATUS_total{value="Requests per sec"} 0.0
# HELP SERVER_STATUS_total Help text
# TYPE SERVER_STATUS_total counter
SERVER_STATUS_total{value="Apache Config Test"} 0.0
```
