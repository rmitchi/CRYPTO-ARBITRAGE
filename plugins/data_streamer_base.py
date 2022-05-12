# Author - Karan Parmar

"""
Base data streamer
"""

# Importing built-in libraries
from threading import Thread

# Importing dependent libraries

# Importing third-party libraries
from websocket import WebSocketApp

class BaseDataStreamer(Thread):

	TYPE = "STREAMER"
	EXCHANGE = "DUMMY"
	
	url = ""

	database = None

	def __init__(self):
		Thread.__init__(self,daemon=False)
		
	def create_websocket_app(self) -> None:
		"""
		Creates websocket app\n
		"""
		self.WSAPP = WebSocketApp(
			self.url,
			on_open=self.on_open,
			on_message=self.on_message,
			on_close=self.on_close,
			on_ping=self.on_ping,
			on_pong=self.on_pong
		)

	def on_open(self,wsapp) -> None:
		"""
		"""
		pass

	def on_message(self,wsapp,message) -> None:
		"""
		"""
		pass

	def on_close(self,wsapp,*args) -> None:
		"""
		"""
		pass
	
	def on_ping(self,*args) -> None:
		"""
		"""
		pass

	def on_pong(self,*args) -> None:
		"""
		"""
		pass

	# Public methods
	def connect_database(self, database):
		"""
		Binds to data saver\n
		"""
		self.database = database

	def set_symbol(self,symbol:str) -> None:
		self.SYMBOL = symbol

	def save_data(self,ltp: float, qty: float) -> None:
		"""
		Saves appropriate data in database\n
		"""
		data = {
			'ltp':ltp,
			'qty':qty,
		}
		self.database.add_stream_data(self.SYMBOL, self.EXCHANGE, data)
		
	# Thread
	def run(self):
		
		self.create_websocket_app()

		self.WSAPP.run_forever()