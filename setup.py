#!/usr/bin/env python3

from setuptools import setup

setup(
	name='monta',
	version='1.1',
	description='Disk mounting shortcut for use with dmenu.',
	author='Renato Oliveira',
	url='https://github.com/renatoliveira/monta',
	include_package_data=True,
	package_data={
		'': [
			'monta',
			'license.txt'
		]
	},
	scripts=[
		'monta/scripts/monta',
		'monta/scripts/desmonta',
		'monta/monta-utils'
	]
)

