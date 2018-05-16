import json
import sys
from os.path import isfile
from pathlib import Path

DEFAULT_PATH = str(Path.home()) + '/.config/monta/config'
if not isfile(DEFAULT_PATH):
	print('CONFIG_NOT_FOUND')
	sys.exit(1)

with open(str(Path.home()) + '/.config/monta/config', 'r') as json_data:
	config = json.load(json_data)
	if 'destinations' not in config:
		print('Configuration file not properly configured.')
		sys.exit(1)
	else:
		for destination in config['destinations']:
			print(destination)

