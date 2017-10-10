#!/usr/bin/env python
# encoding: utf-8


"""
mail:x0hcker@gmail.com
@createtime: 17/9/6 下午11:23
@license: Apache Licence 2.0
usege:
    ......

"""

import os, logging
import os.path
from threading import Thread
from DoraClient.monitor.logged import logged

from DoraClient.plugin.pluginManager import DirectoryPluginManager

__ALL__=["Child","Monitor"]



class Child(Thread):

    def __init__(self, filename):
        Thread.__init__(self)
        self.filename = "{}Plugin".format(filename)


        self.res = None

    def run(self):

        plugin_manager = DirectoryPluginManager()
        plugin_manager.loadPlugins()

        plugin = plugin_manager.getPlugins(self.filename)

        self.res = plugin.execFun()

    def get_result(self):
        return self.res

@logged(logging.DEBUG)
def Monitor(monitor_list=[]):

    result = []

    for monitor in monitor_list:

        t = Child(monitor)
        result.append(t)


    # 启动进程监控各项值标
    for res in result:
        res.start()

    # 等待结果，并收集执行结果
    for res in result:
        res.join()

    data = []
    for res in result:
        data.append(res.get_result())

    return data


# if __name__ == '__main__':
#     clint()
