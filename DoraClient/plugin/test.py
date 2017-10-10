#!/usr/bin/env python
# encoding: utf-8


"""
mail:x0hcker@gmail.com
@createtime: 17/9/6 下午11:36
@license: Apache Licence 2.0
usege:
    ......
    
"""

from DoraClient.plugin.pluginManager import DirectoryPluginManager, URIPluginManager


if __name__ == '__main__':

    plugin_manager = URIPluginManager()
    plugin = plugin_manager.getPlugins("FirstPlugin")


    print (plugin.execFun())