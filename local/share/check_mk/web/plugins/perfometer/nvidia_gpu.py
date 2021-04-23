#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

def perfometer_temperature(row, check_command, perf_data):
    if perf_data[0][4] != "" and float(perf_data[0][4]) < float(perf_data[0][1]):
        color = "#FFBB00"
    elif perf_data[0][3] != "" and float(perf_data[0][3]) < float(perf_data[0][1]):
        color = "#FFBB00"
    else:
        color = "#00FF00"
    curval = float(perf_data[0][1])
    return u"%d °C" % int(curval), perfometer_logarithmic(curval, 40, 1.2, color)
def perfometer_util(row, check_command, perf_data):
    if perf_data[0][4] != "" and float(perf_data[0][4]) < float(perf_data[0][1]):
        color = "#FF0000"
    elif perf_data[0][3] != "" and float(perf_data[0][3]) < float(perf_data[0][1]):
        color = "#FFBB00"
    else:
        color = "#00FF00"
    curval = float(perf_data[0][1])
    legend = "%0.1f%%" % curval
    data = [(curval, color), (100-curval, '#fff')]
    return legend, render_perfometer(data)

perfometers["check_mk-nvidia_gpu.temp"] = perfometer_temperature
perfometers["check_mk-nvidia_gpu.util"] = perfometer_util
perfometers["check_mk-nvidia_gpu.memutil"] = perfometer_util

