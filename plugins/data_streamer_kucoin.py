# Author - Karan Parmar

# Importing built-in libraries
import json

# Importing dependent libraries
from .data_streamer_base import BaseDataStreamer, EXCHANGE

class KucoinDataStreamer(BaseDataStreamer):

	url = "wss://push1-v2.kucoin.com/endpoint"
	exchange = EXCHANGE.KUCOIN	

	def on_open(self, wsapp) -> None:
		data = {
			"id": 1545910660738,
			"type": "subscribe",
			"topic": f"/market/ticker:{self.SYMBOL.replace('_','-')}",
			"privateChannel": False,
			"response": True
		}
		self.WSAPP.send(json.dumps(data))

	def on_message(self, wsapp, message) -> None:
		msg = json.loads(message)
		print(msg)
		self.save_data(float(msg['data']['last']),0)
		print(self.app.prices)

if __name__ == '__main__':
	class App:
		prices = {}

	a = App()

	s1 = KucoinDataStreamer(a)
	s1.start()