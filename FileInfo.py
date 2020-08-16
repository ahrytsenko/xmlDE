import xml.etree.ElementTree as ET

class FileInfo():
	def __init__(self, file):
		self.file_name = file.get("file_name")
		self.description = file.get("description")
		self.file_data = file.text

	def print_info(self):
		print("File name   : " + self.file_name)
		print("Description : " + self.description)
		print("File size   : " + str(len(self.file_data)))

		