# Author - Karan Parmar

# Importing built-in libraries
import importlib

# Importing dependent libraries
from ..core.base import BasePlugin
from ..utils.exceptions import PluginNotFound

class PluginManager:

	_installedPlugins = {}

	# Public methods
	def load_plugin(self, pluginPath:str) -> BasePlugin:
		"""
		Loads plugin class reference from the plugin module path\n
		"""
		slugs = pluginPath.split('.')
		pluginModule, pluginName = '.'.join(slugs[:-1]), slugs[-1]
		try:
			return getattr(importlib.import_module(pluginModule),pluginName)
		except AttributeError:
			raise PluginNotFound

	def get_plugin(self, pluginId:str) -> BasePlugin:
		"""
		Get plugin class reference\n
		"""
		plugin = self._installedPlugins.get(pluginId)
		if plugin: 
			return plugin

		raise PluginNotFound

	def get_all_installed_plugins_by_type(self, pluginType:str) -> list[BasePlugin]:
		"""
		Gets all installed plugins by type\n
		"""
		return [plugin for plugin in self._installedPlugins.values() if plugin.TYPE == pluginType]
	
	def get_all_installed_plugins(self) -> dict:
		"""
		Gets all installed plugins\n
		"""
		return self._installedPlugins

	def sync_plugin(self, plugin:BasePlugin) -> None:
		"""
		Syncs the plugin\n
		"""
		self._installedPlugins[plugin.ID] = plugin
	