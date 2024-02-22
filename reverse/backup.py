import os
from uuid import uuid4
from reverse.compressor import BZ2


class BackupFile:
	def __init__(self, filepath: str, compress_method: str='bz2'):
		self.filepath = filepath
		self.compress_method = compress_method
		self.file_uuid = uuid4()

		self.__check()

	def __check(self) -> None:
		try:
			with open(self.filepath, 'rb') as file:
				data = file.read()
		except FileNotFoundError:
			print('FileNotFound Error. Create file...')
			with open(self.filepath, 'wb') as file:
				data = file.write('0' * 1000)
		
		print(f'[{self.file_uuid}] backup {self.filepath}')

	def save(self) -> bool:
		if self.compress_method == 'bz2':
			archive = BZ2(self.filepath, f'{self.file_uuid}.bz2')
			archive.compress()
			print(f'[{self.file_uuid}] {self.filepath} compressed via bz2 ({self.filepath}.bz)')
			os.system(f'rm {self.filepath}')
		else:
			print('Error: unknown compress method')
			return False

	def unpack(self) -> bool:
		if self.compress_method == 'bz2':
			archive = BZ2(self.filepath, f'{self.file_uuid}.bz2')
			archive.decompress()
			print(f'[{self.file_uuid}] {self.filepath} decompressed via bz2 ({self.filepath}.bz)')
			os.system(f'rm {self.file_uuid}.bz2')
		else:
			print('Error: unknown compress method')
			return False
