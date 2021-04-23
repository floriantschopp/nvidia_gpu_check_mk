#!/usr/bin/env python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

metric_info["GPU_util"] = {
    "title" : _("GPU Utilization"),
    "unit"  : "%",
    "color" : "#00ff00",
}
metric_info["memused"] = {
    "title" : _("GPU Memory used"),
    "unit"  : "bytes",
    "color" : "#00ff00",
}
metric_info["memutil"] = {
    "title" : _("GPU Memory Utilization"),
    "unit"  : "%",
    "color" : "#00ff00",
}
metric_info["temperature"] = {
    "title" : _("GPU Temperature"),
    "unit"  : "c",
    "color" : "#0000ff",
}

check_metrics["nvidia_gpu.util"]                          = {}
check_metrics["nvidia_gpu.memused"]                          = { 0: { "name": "memused", "scale" : MB} }
check_metrics["nvidia_gpu.memutil"]                          = {}
check_metrics["nvidia_gpu.temp"]                          = {}
perfometer_info.append(("linear", ("temperature", 40.0, None)))
perfometer_info.append(("linear", ("GPU_util", 100, None)))
