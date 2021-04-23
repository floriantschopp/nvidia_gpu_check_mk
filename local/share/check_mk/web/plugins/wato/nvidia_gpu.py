#!/usr/bin/env python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

register_rule("agents/" + _("Agent Plugins"),
    "agent_config:nvidia_gpu",
    DropdownChoice(
        title = _("Nvidia GPU (Linux)"),
        help = _("This will deploy the agent plugin <tt>nvidia_gpu</tt> to collect GPU utilization values."),
        choices = [
            ( True, _("Deploy plugin for GPU Monitoring") ),
            ( None, _("Do not deploy plugin for GPU Monitoring") ),
        ]
    )
)
