# Author - Karan Paramra

"""
Data streaming Interface\n
"""

from ...utils.enums import KEY

class IDataStreaming:

	# Public methods
	def connect_database(self, database):
		"""
		Connects to database\n
		"""
		self.database = database

	def set_symbol(self,symbol:str) -> None:
		self.SYMBOL = symbol

	def save_data(self,ltp: float, qty: float) -> None:
		"""
		Saves appropriate data in database\n
		"""
		data = {
			KEY.LTP:ltp,
			KEY.QUANTITY:qty,
		}
		self.database.add_stream_data(self.SYMBOL, self.MARKET, self.EXCHANGE, data)