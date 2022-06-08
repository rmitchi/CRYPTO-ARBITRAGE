# Author - Karan Parmar

"""
Constants
"""

from pathlib import PurePath

from .enums import LOG_TYPE

BASE_DIR = PurePath(__file__).parent.parent
BASE_DIR_NAME = BASE_DIR.name

DEFAULT_TIMEZONE = "UTC"
DEFAULT_REFRESH_RATE = 1

DEFAULT_LOGS_FILE_NAME = "logs.csv"

LOGS_TO_EXCLUDE_PRINTING = [
	LOG_TYPE.INFO, 
	LOG_TYPE.TERMINAL,
]

# NOTE INTERNAL PLUGINS THAT MUST BE LOADED
INTERNAL_PLUGINS = [
	f"{BASE_DIR_NAME}.core.plugins.BinanceDataStreamerSpot",
	f"{BASE_DIR_NAME}.core.plugins.FTXDataStreamerSpot",
	f"{BASE_DIR_NAME}.core.plugins.HuobiDataStreamerSpot",
	f"{BASE_DIR_NAME}.core.plugins.KrakenDataStreamerSpot",
	f"{BASE_DIR_NAME}.core.plugins.KucoinDataStreamerSpot",
	f"{BASE_DIR_NAME}.core.plugins.BinanceDataStreamerFutures",
	f"{BASE_DIR_NAME}.core.plugins.FTXDataStreamerFutures",
	f"{BASE_DIR_NAME}.core.plugins.HuobiDataStreamerFutures",
	f"{BASE_DIR_NAME}.core.plugins.KrakenDataStreamerFutures",
	f"{BASE_DIR_NAME}.core.plugins.KucoinDataStreamerFutures",
]


# NOTE DEFAULT PLUGINS TO BE USED IN THE APP, IF NOT SPECIFIED