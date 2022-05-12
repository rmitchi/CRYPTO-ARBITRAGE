# Author - Karan Parmar

# Importing built-in libraries
import json

# Importing dependent libraries
from .data_streamer_base import BaseDataStreamer, EXCHANGE

class OKEXDataStreamer(BaseDataStreamer):

	url = "wss://ws.kraken.com/"
	exchange = EXCHANGE.OKEX	

	def on_open(self, wsapp) -> None:
		data = {
			"event":"subscribe", 
			"subscription":{"name":"ticker"}, 
			"pair":[self.SYMBOL.replace("_","/")]
		}
		self.WSAPP.send(json.dumps(data))

	def on_message(self, wsapp, message) -> None:
		msg = json.loads(message)
		print(msg)
		self.save_data(float(msg['data']['last']),0)
		
if __name__ == '__main__':
	class App:
		prices = {}

	a = App()

	s1 = OKEXDataStreamer(a)
	s1.start()