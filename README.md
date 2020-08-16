# xmlDE
XML Document Extractor

Purpose
XML Document Extractor allows to obtain files embedded into the XML-container.
The valid structure listed below.
XML containers will be taken from ./data directory
Extracted files will be stored in ./files directory

Command line example:
xmkDE.py [xml_file_01.xml [xml_file_02.xml ...[xml_file_nn.xml]]]

Valid XML structure
<code>
< Header
	msg_id="some-message-id"
  	from_org_id="12345678"
  	from_organization="TEXT"
  	to_org_id="12345609"
  	to_organization="TEXT2" >
	< Document
    	idnumber="1"
    	annotation="TEXT" >
    	< DocTransfer
      		file_name="file_name1.ext"
      		description="File_Description" >
      		Base64_Encoded_File_Content
  		< /DocTransfer >
    	< DocTransfer
      		file_name="file_name2.ext"
      		description="File_Description" >
      		Base64_Encoded_File_Content
  		< /DocTransfer >
    	< DocTransfer
      		file_name="file_name3.ext"
      		description="File_Description" >
      		Base64_Encoded_File_Content
  		< /DocTransfer >
    < /Document >
	< Document
    	idnumber="2"
    	annotation="TEXT">
    	< DocTransfer
      		file_name="file_name4.ext"
      		description="File_Description" >
      		Base64_Encoded_File_Content
  		< /DocTransfer >
    	< DocTransfer
      		file_name="file_name5.ext"
      		description="File_Description" >
      		Base64_Encoded_File_Content
  		< /DocTransfer >
    	< DocTransfer
      		file_name="file_name6.ext"
      		description="File_Description" >
      		Base64_Encoded_File_Content
  		< /DocTransfer >
    < /Document >
< /Header >
</code>