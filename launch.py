# Author - Karan Parmar

"""
Launch
"""

# Importing built-in libraries
import os, json

# Importing dependent libraries
from varitrage import App

def main():

	# Creds
	with open(os.path.join(os.getcwd(),'credentials.json')) as f:
		creds = json.load(f)
		f.close()

	# Config
	with open(os.path.join(os.getcwd(),'config.json')) as f:
		config = json.load(f)
		f.close()

	# APP Config
	with open(os.path.join(os.getcwd(),'app_config.json')) as f:
		app_config = json.load(f)
		f.close()

	# Symbol data
	with open(os.path.join(os.getcwd(),'symbol_data.json')) as f:
		symbol_data = json.load(f)
		f.close()

	app = App(creds=creds, config=config, app_config=app_config, symbol_data=symbol_data)

	app.start()

if __name__ == '__main__':
	main()