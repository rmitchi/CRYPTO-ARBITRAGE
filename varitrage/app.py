# Author - Karan Parmar

"""
CRYPTO ARBITRAGE APP
"""

# Importing built-in libraries
import os, time
from datetime import datetime

# Importing dependent libraries
from .components import StreamManager, DatabaseManager, PluginManager, LogManager
from .utils.enums import APP_KEY, LOG_TYPE
from .utils.constants import DEFAULT_TIMEZONE, DEFAULT_REFRESH_RATE, DEFAULT_LOGS_FILE_NAME

from websocket import WebSocketApp
import threading, json


url = "ws://127.0.0.1:8000/connect"
ws = WebSocketApp(url)

t = threading.Thread(target=ws.run_forever)
t.start()

class App:
	
	TIMEZONE = DEFAULT_TIMEZONE
	REFRESH_RATE = DEFAULT_REFRESH_RATE

	def __init__(self, *, creds:dict, config:dict, app_config:dict, **options):
		
		self.CREDS  = creds
		self.CONFIG = config
		self.APP_CONFIG = app_config
		self.SYMBOL_DATA = options.get('symbol_data')

		self.WATCHLIST = self.CONFIG[APP_KEY.WATCHLIST].copy()
		self.MARKETS = self.CONFIG[APP_KEY.MARKETS].copy()

		self.REFRESH_RATE = self.APP_CONFIG.get(APP_KEY.REFRESH_RATE, self.REFRESH_RATE)

		# COMPONENTS
		self.PluginManager = PluginManager()
		self.StreamManager = StreamManager()
		self.DatabaseManager = DatabaseManager()

		self.initialize()

	# Helper methods

	# Private methods
	def _record_prices(self) -> None:
		"""
		Records prices of the block\n
		"""
		current_time = int(datetime.now().timestamp()*1000)
		
		prices = {APP_KEY.TIMESTAMP:current_time}

		for watch in self.WATCHLIST:
			for market, exchanges in self.MARKETS.items():
				prices[market] = {}
				for exchange in exchanges:
					try:
						prices[market].update({exchange:self.DatabaseManager.get_data()[market][watch][exchange][APP_KEY.LTP]})
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

		# Initialize log manager
		LogManager.set_timezone(self.TIMEZONE)
		LogManager.set_logs_directory(logs_directory_path=os.getcwd())
		LogManager.set_logs_file_name(logs_file_name=DEFAULT_LOGS_FILE_NAME)
		LogManager.initialize()

		# Load internal and external plugins
		self.PluginManager.load_all_internal_plugins()
		self.log(LOG_TYPE.SUCCESS, "Loaded internal plugins")
		self.PluginManager.load_all_external_plugins(self.APP_CONFIG[APP_KEY.PLUGINS])
		self.log(LOG_TYPE.SUCCESS, "Loaded external plugins")

		# Initializing database manager
		self.DatabaseManager.set_symbol_data(self.SYMBOL_DATA)

		# Initializing stream manager
		self.StreamManager.set_watchlist(self.WATCHLIST)
		self.StreamManager.set_markets(self.MARKETS)
		self.StreamManager.connect_app(self)
		self.StreamManager.start_streamers()
		self.StreamManager.subscribe_to_tickers()

	def log(self, log_type:str, message:str) -> None:
		"""
		Logs the message\n
		"""
		LogManager.log(log_type, message)

	def start(self) -> None:
		"""
		Start the app\n
		"""
		while True:
			self._record_prices()
			time.sleep(self.REFRESH_RATE)