#!/usr/bin/python3

import sys, getopt
from os import path
import xml.etree.ElementTree as ET
from Message import Message
import base64

DATA_FOLDER = "./data/"
FILES_FOLDER = "./files/"
FILES_TO_PROCESS = []
SCRIPT_NAME = sys.argv[0]
HELP_STRING = "Example: " + SCRIPT_NAME + " [<file_name.xml> [<file_name.xml> [...] ] ]\n"

class XMLDocumentExtractor():
	def __init__(self, file_name):
		self.file_name = file_name
		self.msg = []

	# Check if file has a valid XML structure
	# Returns True if success
	# Parsed file content stored in msg 
	def xml_file_valid(self):
		try:
			tree = ET.parse(self.file_name)
			root = tree.getroot()
			#print(root.get("version"))
			self.msg = Message(root)
		except:
			return False
		return True


	def process_xml_file(self):
		print("Processing file " + self.file_name + " ...")
		if self.xml_file_valid():
			self.msg.print_header()
			for file in self.msg.files:
				f = open(FILES_FOLDER + file.file_name, "wb")
				f.write(base64.b64decode(file.file_data))
				f.close()
		else:
			print(" Given file " + self.file_name + " is invalid or corrupted.")
		print("Done\n")


# Check if files to process were specified in command line
# Returns True if at least one specified file is exists
# Otherwise returns False
# Existed files were stored in FILES_TO_PROCESS list
def arguments_valid(argv):
	for arg in argv:
		if path.exists(DATA_FOLDER + arg):
			FILES_TO_PROCESS.append(DATA_FOLDER + arg)
		else:
			print("Error: file '" + DATA_FOLDER + arg + "' not found.\n")

	return (len(FILES_TO_PROCESS) > 0)


# Entry point
def main(argv):
	if arguments_valid(argv[1:]):
		for xml_file in FILES_TO_PROCESS:
			xmlDE = XMLDocumentExtractor(xml_file)
			xmlDE.process_xml_file()
	else:
		print(HELP_STRING)


if __name__ == '__main__':
	main(sys.argv)