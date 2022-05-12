# Author - Karan Parmar

"""
CRYPTO ARBITRAGE APP
"""

# Importing built-in libraries
import time
from datetime import datetime

# Importing dependent libraries
from .components import StreamManager, DatabaseManager, PluginManager
from .utils.enums import KEY

from websocket import WebSocketApp
import threading, json


def on_close(*args):
	print('close')
	print(args)

def on_error(*args):
	print('error')
	print(args)

url = "ws://127.0.0.1:8000/connect"
ws = WebSocketApp(url,on_close=on_close,on_error=on_error)

t = threading.Thread(target=ws.run_forever)
t.start()

class App:

	APP_CONFIG = {
		KEY.PLUGINS:[]
	}

	_refreshRate = 0.5

	def __init__(self,creds:dict,config:dict,*,appConfig:dict=None):
		
		self.CREDS  = creds
		self.CONFIG = config
		self.APP_CONFIG = appConfig or self.APP_CONFIG

		self.WATCHLIST = self.CONFIG[KEY.WATCHLIST].copy()
		self.MARKETS = self.CONFIG[KEY.MARKETS].copy()

		self._refreshRate = config.get(KEY.REFRESH_RATE,self._refreshRate)

		# COMPONENTS
		self.pluginManager = PluginManager()
		self.streamManager = StreamManager()
		self.databaseManager = DatabaseManager()

		self.initialize()

	# Helper methods

	# Private methods
	def _record_prices(self) -> None:
		"""
		Records prices of the block\n
		"""
		currentTime = int(datetime.now().timestamp()*1000)
		
		prices = {KEY.TIMESTAMP:currentTime}

		for watch in self.WATCHLIST:
			for market, exchanges in self.MARKETS.items():
				prices[market] = {}
				for exchange in exchanges:
					try:
						prices[market].update({exchange:self.databaseManager.get_data()[market][watch][exchange][KEY.LTP]})
					except KeyError:
						break
		# try:
		# 	prices['AVG'] = sum([prices[i] for i in self.EXCHANGES]) / 3
		# except KeyError:
		# 	pass
		print(prices)
		try:
			ws.send(json.dumps(prices))
		except Exception:
			pass
		
	# Public methods
	def initialize(self) -> None:
		"""
		Initializes app instance\n
		"""

		self.sync_plugins()

		self.streamManager.set_watchlist(self.WATCHLIST)
		self.streamManager.set_markets(self.MARKETS)
		self.streamManager.connect_app(self)
		self.streamManager.start_streamers()

	def sync_plugins(self) -> None:
		"""
		Sync all the plugins in the app\n
		"""
		for pluginPath in self.APP_CONFIG[KEY.PLUGINS]:
			plugin = self.pluginManager.load_plugin(pluginPath)
			self.pluginManager.sync_plugin(plugin)

	def start(self) -> None:
		"""
		Start the app\n
		"""
		while True:
			self._record_prices()
			time.sleep(self._refreshRate)