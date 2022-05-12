# Author - Karan Parmar

"""
Enums
"""

class KEY:

	DUMMY = 'dummy'
	
	TIMESTAMP = 'timestamp'
	LTP = 'ltp'
	QUANTITY = 'quantity'
	REFRESH_RATE = 'refresh_rate'
	WATCHLIST = 'watchlist'
	MARKETS = "markets"
	EXCHANGES = 'exchanges'
	PLUGINS = 'plugins'

class EXCHANGE:

	EXCHANGE = 'EXCHANGE'
	BINANCE = 'BINANCE'
	FTX = 'FTX'
	KUCOIN = 'KUCOIN'
	HUOBI = 'HUOBI'
	KRAKEN = 'KRAKEN'
	OKEX = 'OKEX'

class CATEGORY:

	SPOT = "SPOT"
	FUTURES = "FUTURES"

class PLUGIN:

	ID = "ID"
	TYPE = "TYPE"

class PLUGIN_TYPE:

	STREAMER = "STREAMER"
	BROKER_API = "BROKER_API"

class STREAMER_INTERFACE:
	
	CONNECT_DATABASE = "connect_database"
	SAVE_DATA = "save_data"