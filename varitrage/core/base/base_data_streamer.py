# Author - Karan Parmar

"""
Base data streamer plugin\n
"""

# Importing built-in libraries
from threading import Thread

# Importing dependent libraries
from . import BasePlugin
from ..interfaces import IWebsocketApp, IDataStreaming
from ...utils.enums import PLUGIN_TYPE, EXCHANGE

class BaseDataStreamer(Thread, BasePlugin, IWebsocketApp, IDataStreaming):

	TYPE = PLUGIN_TYPE.STREAMER
	EXCHANGE = EXCHANGE.EXCHANGE

	def __init__(self):
		Thread.__init__(self,daemon=False)

	# Thread
	def run(self):
		
		self.create_websocket_app()

		self.WSAPP.run_forever()