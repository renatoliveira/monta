from drive_list import get_description
from sys import argv
from sys import exit
from subprocess import check_output


def get_drive_by_name(drive_name):
	disks = get_description()
	for disk in disks['blockdevices']:
		for partition in disk['children']:
			if partition['label'] == argv[1]:
				return partition['name']

if __name__ == '__main__':
	print(get_drive_by_name(argv[1]))

