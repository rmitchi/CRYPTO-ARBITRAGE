# Author - Karan Parmar

"""
Stream Manager
"""

# Importing dependent libraries
from ..core.interfaces import IDataStreaming
from ..utils.enums import STREAMER_INTERFACE, PLUGIN, PLUGIN_TYPE, LOG_TYPE

class StreamManager:
	
	database = None

	_markets = {}
	_watchlist = []
	_streamers = {}

	# Private methods
	def _start_single_streamer(self, market:str, exchange:str, streamer_id:str) -> bool:
		"""
		Start a single streamer inside a thread\n
		"""
		Plugin = self.app.PluginManager.get_plugin(streamer_id)
		if Plugin:
			self._implement_streamer_attributes(Plugin)
			
			self._streamers[market][exchange] = Plugin()
			self._streamers[market][exchange].connect_database(self.app.DatabaseManager)
			self._streamers[market][exchange].start()

			return True
		else:
			return False

	def _implement_streamer_attributes(self, Plugin) -> None:
		"""
		Implements base attributes to a streamer\n
		"""
		setattr(Plugin, PLUGIN.TYPE, PLUGIN_TYPE.STREAMER)
		setattr(Plugin, STREAMER_INTERFACE.CONNECT_DATABASE, IDataStreaming.connect_database)
		setattr(Plugin, STREAMER_INTERFACE.SAVE_DATA, IDataStreaming.save_data)
		
	# Public methods
	def set_watchlist(self, watchlist:list) -> None:
		"""
		Sets watchlist to get data for those watch\n
		"""
		self._watchlist = watchlist

	def set_markets(self, markets:list) -> None:
		"""
		Sets markets from which streamming data will be fetched\n
		"""
		self._markets = markets

	def connect_app(self, app) -> None:
		"""
		Connects to app instance\n
		"""
		self.app = app

	def start_streamers(self) -> None:
		"""
		Starts all streamers in a separate thread\n
		"""
		for market, exchanges in self._markets.items():
			self._streamers[market] = {}
			
			for exchange, streamer_id in exchanges.items():
				try:
					if self._start_single_streamer(market=market, exchange=exchange, streamer_id=streamer_id):
						self.app.log(LOG_TYPE.STARTED, f"{exchange} {market} streamer")
				
				except Exception:
					continue
	
	def subscribe_to_tickers(self) -> None:
		"""
		Subscribe to tickers\n
		"""
		for market, exchanges in self._markets.items():
			for exchange in exchanges:
				for watch in self._watchlist:
					self._streamers[market][exchange].subscribe(watch)
					self.app.log(LOG_TYPE.SUBSCRIBED, f"{watch} {exchange} {market}")