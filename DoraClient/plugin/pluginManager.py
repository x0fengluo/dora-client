#!/usr/bin/env python
# encoding: utf-8


"""
mail:x0hcker@gmail.com
@createtime: 17/9/6 下午11:23
@license: Apache Licence 2.0
usege:
    ......
    
"""

from DoraClient.plugin.iPlugin import Plugin
import importlib
import importlib.util
import os
import sys


class PluginManager(object):
    """Base class for plugin managers. Does not implement loadPlugins, so it
    may only be used with a static list of plugins.
    """
    name = "base"

    def __init__(self, plugins=(), config={}):
        self.__plugins = []
        if plugins:
            self.addPlugins(plugins)

    def __iter__(self):
        return iter(self.plugins)

    def addPlugin(self, plug):
        # print 'PluginManager add plugin:', plug
        self.__plugins.append(plug)

    def addPlugins(self, plugins):
        for plug in plugins:
            self.addPlugin(plug)

    def delPlugin(self, plug):
        if plug in self.__plugins:
            self.__plugins.remove(plug)

    def delPlugins(self, plugins):
        for plug in plugins:
            self.delPlugin(plug)

    def getPlugins(self, name=None):

        self.loadPlugins(name)
        print(self.__plugins)
        for plugin in self.__plugins:

            if (name is None or plugin.name == name):
                 return  plugin
        return False

    def _loadPlugin(self, plug):
        loaded = False

        for p in self.plugins:
            if p.name == plug.name:
                loaded = True
                break
        if not loaded:
            self.addPlugin(plug)


    def loadPlugins(self):
        pass

    def _get_plugins(self):
        return self.__plugins

    def _set_plugins(self, plugins):
        self.__plugins = []
        self.addPlugins(plugins)

    plugins = property(_get_plugins, _set_plugins, None,
                       """Access the list of plugins managed by
                       this plugin manager""")


class DirectoryPluginManager(PluginManager):
    """Plugin manager that loads plugins from plugin directories.
    """
    name = "directory"

    def __init__(self, plugins=(), config={}):
        default_directory = os.path.join(os.path.dirname(__file__), "plugins")
        self.directories = config.get("directories", (default_directory,))
        # print '========DirectoryPlugManager========', plugins
        PluginManager.__init__(self, plugins, config)

    def loadPlugins(self, plugin_name=None):
        """Load plugins by iterating files in plugin directories.
        """
        plugins = []

        for dir in self.directories:
            try:
                for f in os.listdir(dir):
                    if plugin_name == f[:-3]:
                        plugins.append((plugin_name, dir))
            except OSError:

                continue

        fh = None
        mod = None

        for (module_name, file_path) in plugins:

            old = sys.modules.get(module_name)
            if old is not None:
                del sys.modules[module_name]

            file_path = "{}/{}.py".format(file_path,module_name)


            spec = importlib.util.spec_from_file_location(module_name, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            sys.modules[module_name] = module



            if hasattr(module, "__all__"):
                print(module)
                attrs = [getattr(module, x) for x in module.__all__]

                for plug in attrs:

                    if not issubclass(plug, Plugin):
                        continue
                    self._loadPlugin(plug())


class URIPluginManager(PluginManager):
    """Plugin manager that loads plugins from plugin uri.
    """
    name = "uri"

    def __init__(self, plugins=(), config={}):
        default_directory = os.path.join(os.path.dirname(__file__), "plugins")
        self.directories = config.get("directories", (default_directory,))

        PluginManager.__init__(self, plugins, config)

    def loadPlugins(self, plugin_name=None):
        """Load plugins by iterating files in plugin directories.
        """
        import sys
        import importlib
        from  DoraClient.plugin import  urlimport

        urlimport.install_path_hook()

        sys.path.append('http://localhost:15000')


        module = getattr(importlib.import_module(plugin_name),plugin_name)()
        #print(module)
        self._loadPlugin(module)



