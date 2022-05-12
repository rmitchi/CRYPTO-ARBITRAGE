# Author - Karan Parmar

"""
CONSTANTS
"""

from ..plugins.streamers import *
from .enums import EXCHANGE

CONFIG_FILE_PATH = "config.json"

BINANCE_MARKET_DATA_STREAM_WS_URL = "wss://stream.binance.com:9443"


DATA_STREAMERS = {
	EXCHANGE.BINANCE : BinanceDataStreamer,
	EXCHANGE.FTX : FTXDataStreamer,
	EXCHANGE.KUCOIN : KucoinDataStreamer,
	EXCHANGE.KRAKEN : KrakenDataStreamer,
	EXCHANGE.HUOBI : HuobiDataStreamer,
	EXCHANGE.OKEX : OKEXDataStreamer
}