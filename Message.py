import xml.etree.ElementTree as ET
from Document import Document
from FileInfo import FileInfo

class Message():
	def __init__(self, xml_tree_root):
		self.msg_id = xml_tree_root.get("msg_id")
		self.from_org_id = xml_tree_root.get("from_org_id")
		self.from_organization = xml_tree_root.get("from_organization")
		self.to_org_id = xml_tree_root.get("to_org_id")
		self.to_organization = xml_tree_root.get("to_organization")
		self.documents = []
		self.files = []
		for el in xml_tree_root.findall("Document"):
			self.documents.append(Document(el))
			for file in el.findall("DocTransfer"):
				self.files.append(FileInfo(file))


	def print_header(self):
		print("Message ID      : " + self.msg_id)
		print("Message from    : " + self.from_organization)
		print("Message to      : " + self.to_organization)
		print("Documents found : " + str(len(self.documents)))
		for document in self.documents:
			print(" ID         : " + document.idnumber)
			print(" Annotation : " + document.annotation)
		print("Files found     : " + str(len(self.files)))
		for file in self.files:
			print(" File name : " + file.file_name)
			

