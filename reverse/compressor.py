import bz2


class BZ2:
	def __init__(self, input_file: str, output_file: str):
		self.input_file = input_file
		self.output_file = output_file

	def compress(self):
		with open(self.input_file, 'rb') as fin:
			data = fin.read()
			with bz2.open(self.output_file, 'wb') as fout:
				fout.write(data)

	def decompress(self):
		with bz2.open(self.output_file, 'rb') as fin:
			data = fin.read()
			with open(self.input_file, 'wb') as fout:
				fout.write(data)
