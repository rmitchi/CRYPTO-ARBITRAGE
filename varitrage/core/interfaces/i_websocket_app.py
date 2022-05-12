# Author - Karan Parmar

"""
Websocket app interface
"""

# Importing third-party libraries
from websocket import WebSocketApp

class IWebsocketApp:

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
		Called when ws is opened\n
		"""
		pass

	def on_message(self,wsapp,message) -> None:
		"""
		Called when ws receives any message\n
		"""
		pass

	def on_close(self,wsapp,*args) -> None:
		"""
		Called when ws closes connection\n
		"""
		pass
	
	def on_ping(self,*args) -> None:
		"""
		On ping to server\n
		"""
		pass

	def on_pong(self,*args) -> None:
		"""
		On pong to server\n
		"""
		pass