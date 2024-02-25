#!/usr/bin/python3
from reverse.backup import BackupFile


def main():
	backup = BackupFile('data', compress_method='lzma')
	backup.save()
	backup.unpack()


if __name__ == '__main__':
	main()
