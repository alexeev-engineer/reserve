#!/usr/bin/python3
from reverse.backup import BackupFile


def main():
	backup = BackupFile('data')
	backup.save()
	backup.unpack()


if __name__ == '__main__':
	main()
