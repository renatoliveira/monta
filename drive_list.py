import json
from subprocess import check_output


def get_description():
	return json.loads(check_output('lsblk -pJf'.split(' ')))

def get_drives():
	disks = get_description()

	if 'blockdevices' in disks:
		for disk in disks['blockdevices']:
			for partition in disk['children']:
				if partition['label'] != None:
					print(partition['label'])

if __name__ == '__main__':
	get_drives()

