import xml.etree.ElementTree as ET

class Document():
	def __init__(self, xml_document):
		self.idnumber = xml_document.get("idnumber")
		self.annotation = xml_document.get("annotation")
		self.files = xml_document.findall("DocTransfer") 

	def print_info(self):
		print("ID number   : " + self.idnumber)
		print("Aannotation : " + self.annotation)
		print("File(s)     : " + str(len(self.files)))

