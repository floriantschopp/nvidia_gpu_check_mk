# nvidia_gpu_check_mk

For now, just added all potentially relevant files that were found under `/opt/omd/sites/monitoring`.
Most likely, not all files are necessary, maybe check [here](https://github.com/modusoft/lm-sensors)!

```
$ sudo find . | grep nvidia_gpu
./local/share/check_mk/agents/plugins/nvidia_gpu
./local/share/check_mk/agents/bakery/nvidia_gpu
./local/share/check_mk/web/plugins/wato/nvidia_gpu.py
./local/share/check_mk/web/plugins/perfometer/nvidia_gpu.py
./local/share/check_mk/web/plugins/metrics/nvidia_gpu.py
./local/share/check_mk/checks/nvidia_gpu
./var/check_mk/precompiled_checks/local/check_nvidia_gpu
./var/check_mk/precompiled_checks/local/nvidia_gpu
./var/check_mk/packages/nvidia_gpu
```
