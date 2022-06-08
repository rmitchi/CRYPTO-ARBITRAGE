# Author - Karan Paramra

"""
Data streaming Interface\n
"""

from ...utils.enums import APP_KEY

class IDataStreaming:

	# Public methods
	def connect_database(self, database):
		"""
		Connects to database\n
		"""
		self.database = database

	def save_data(self, symbol:str, ltp: float, qty: float) -> None:
		"""
		Saves appropriate data in database\n
		"""
		data = {
			APP_KEY.LTP:ltp,
			APP_KEY.QUANTITY:qty,
		}
		self.database.add_stream_data(symbol, self.MARKET, self.EXCHANGE, data)