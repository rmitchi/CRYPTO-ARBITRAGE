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
		appConfig = json.load(f)
		f.close()

	app = App(creds,config,appConfig=appConfig)

	app.start()

if __name__ == '__main__':
	main()