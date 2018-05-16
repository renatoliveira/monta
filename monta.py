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

# first arg is 'monta.py', the second one is the drive name and the third arg is the destination path
def main():
	if len(argv) != 3:
		print('Incorrect number of args in "argv".')
		exit(1)
	print(argv)
	mount_result = check_output('mount {0} {1}'.format(get_drive_by_name(
		argv[1]),
		argv[0]
	).split(' '))

if __name__ == '__main__':
	main()

