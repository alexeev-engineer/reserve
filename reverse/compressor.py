import bz2
import lzma


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


class LZMA:
	def __init__(self, input_file: str, output_file: str):
		self.input_file = input_file
		self.output_file = output_file
		self.lzc = lzma.LZMACompressor()
		self.lzd = lzma.LZMADecompressor()

	def compress(self):
		with open(self.input_file) as fin:
			with open(self.output_file, "wb") as fout:
				for chunk in fin.read(1024):
					compd_chunk = self.lzc.compress(chunk.encode("utf-8"))
					fout.write(compd_chunk)
				fout.write(self.lzc.flush())

	def decompress(self):
		lzd = lzma.LZMADecompressor()
		strings = ""
		with open(self.output_file, "rb") as f:
			data = lzd.decompress(f.read())
			strings += data[:5].decode("utf-8")
			with open(self.input_file, 'w') as fin:
				fin.write(strings)
