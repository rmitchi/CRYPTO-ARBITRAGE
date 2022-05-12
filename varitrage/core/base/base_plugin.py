# Author - Karan Parmar

from abc import ABCMeta, abstractmethod
from ...utils.enums import PLUGIN
from ...utils.exceptions import PluginChangeAccessDenied

class BasePlugin(metaclass=ABCMeta):

	@property
	@abstractmethod
	def ID(cls):
		pass

	@property
	@abstractmethod
	def TYPE(cls):
		pass

	@property
	@abstractmethod
	def NAME(cls):
		pass

	@property
	@abstractmethod
	def AUTHOR(cls):
		pass

	def __setattr__(self, __name, __value):
		if __name in [PLUGIN.ID,PLUGIN.TYPE]:
			raise PluginChangeAccessDenied
		else:
			object.__name = __value
