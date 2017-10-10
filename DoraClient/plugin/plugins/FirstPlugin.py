#!/usr/bin/env python
# encoding: utf-8


"""
mail:x0hcker@gmail.com
@createtime: 17/9/6 下午11:28
@license: Apache Licence 2.0
usege:
    ......
    
"""

import sys


from DoraClient.plugin.iPlugin import Plugin

__all__ = ["FirstPlugin"]


class FirstPlugin(Plugin):
    """
    测使用
    """
    name = "FirstPlugin"
    version = '0.0.1'

    def __init__(self):

        Plugin.__init__(self)

    def scan(self, config={}):
        return "first plugin"

    def execFun(self):
        return "exec function"
    