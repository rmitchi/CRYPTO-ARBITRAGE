# Author - Karan Parmar

"""
Stream Manager
"""

# Importing dependent libraries
from ..core.interfaces import IDataStreaming
from ..utils.enums import STREAMER_INTERFACE, PLUGIN, PLUGIN_TYPE

class StreamManager:
	
	database = None

	_markets = {}
	_watchlist = []
	_streamers = {}

	# Private methods
	def _start_single_streamer(self, watch:str, market:str, exchange:str, streamerId:str) -> bool:
		"""
		Start a single streamer inside a thread\n
		"""
		Plugin = self.app.pluginManager.get_plugin(streamerId)
		if Plugin:
			self._implement_streamer_attributes(Plugin)

			self._streamers[watch][market][exchange] = Plugin()
			self._streamers[watch][market][exchange].set_symbol(watch)
			self._streamers[watch][market][exchange].connect_database(self.app.databaseManager)
			self._streamers[watch][market][exchange].start()
			return True
		else:
			return False

	def _implement_streamer_attributes(self,Plugin) -> None:
		"""
		Implements base attributes to a streamer\n
		"""
		setattr(Plugin,PLUGIN.TYPE,PLUGIN_TYPE.STREAMER)
		setattr(Plugin,STREAMER_INTERFACE.CONNECT_DATABASE,IDataStreaming.connect_database)
		setattr(Plugin,STREAMER_INTERFACE.SAVE_DATA,IDataStreaming.save_data)
		
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
		for watch in self._watchlist:
			
			self._streamers[watch] = {}

			for market, exchanges in self._markets.items():
				self._streamers[watch][market] = {}
				
				for exchange, streamerId in exchanges.items():
					try:
						if exchange not in self._streamers[watch]:
							if self._start_single_streamer(watch=watch,market=market,exchange=exchange,streamerId=streamerId):
								print(f'{exchange} started')
					
					except Exception:
						continue
			