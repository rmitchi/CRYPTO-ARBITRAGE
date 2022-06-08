# Author - Karan Paramr

"""
Database manager

- Manages data
- Handles symbols uncertainity
"""

class DatabaseManager:

	symbol_data = {}

	db = {}
	
	def set_symbol_data(self, symbol_data:dict) -> None:
		"""
		Set symbol data\n
		"""
		self.symbol_data = symbol_data

	def add_stream_data(self, symbol:str, market:str, exchange:str, data:dict) -> None:
		"""
		Adds stream data to database\n
		"""
		symbol = self.symbol_data[market][exchange][symbol]
		if market not in self.db: self.db[market] = {}
		if symbol not in self.db[market]: self.db[market][symbol] = {}
		if exchange not in self.db[market][symbol]: self.db[market][exchange] = []

		self.db[market][symbol][exchange] = data

	def get_data(self, *, watch:str=None, exchange:str=None) -> dict:
		"""
		Returns data of saved ticks\n
		"""
		return self.db