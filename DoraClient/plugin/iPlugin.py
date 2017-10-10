#!/usr/bin/env python
# encoding: utf-8


"""
mail:x0hcker@gmail.com
@createtime: 17/9/6 下午11:23
@license: Apache Licence 2.0
usege:
    ......
    
"""

class Plugin(object):
    """ 定义一个接口，其他 插件必须实现这个接口，name 属性必须赋值 """
    name = ''
    description = ''
    version = ''

    def __init__(self):
        pass


    def executeFun(self):
        pass