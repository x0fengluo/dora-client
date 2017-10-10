#!/usr/bin/env python
# encoding: utf-8


"""
mail:x0hcker@gmail.com
@createtime: 17/9/6 下午11:23
@license: Apache Licence 2.0
usege:
    ......

"""

import sys


from DoraClient.plugin.iPlugin import Plugin

__all__ = ["CpuUsedPlugin"]


class CpuUsedPlugin(Plugin):
    """
    CpuUsedPlugin 用于监控cpu使用率
    """
    name = "CpuUsedPlugin"
    version = '0.0.1'

    def __init__(self):
        Plugin.__init__(self)

    def scan(self, config={}):
        return "CpuUsed plugin"

    def execFun(self):
        return "exec CpuUsed"