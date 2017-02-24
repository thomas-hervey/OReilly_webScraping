# #reading CSV
# from urllib.request import urlopen
# from io import StringIO
# import csv

# data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')
# dataFile = StringIO(data)
# dictReader = csv.DictReader(dataFile)

# print(dictReader.fieldnames)

# for row in dictReader:
# 	print(row)


# #reading PDF
# from urllib.request import urlopen
# from pdfminer.pdfinterp import PDFResourceManager, process_pdf
# from pdfminer.converter import TextConverter
# from pdfminer.layout import LAParams
# from io import StringIO, open

# def readPDF(pdfFile):
# 	rsrcmgr = PDFResourceManager()
# 	retstr = StringIO()
# 	laparams = LAParams()
# 	device = TextConverter(rsrcmgr, retstr, laparams=laparams)

# 	process_pdf(rsrcmgr, device, pdfFile)
# 	device.close()

# 	content = retstr.getvalue()
# 	retstr.close()
# 	return content

# pdfFile = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")
# outputString = readPDF(pdfFile)
# print(outputString)
# pdfFile.close()


#reading .docx ~support is bad so we made our own solution
from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
from bs4 import BeautifulSoup

wordFile = urlopen("http://pythonscraping.com/pages/AWordDocument.docx").read()
wordFile = BytesIO(wordFile)
document = ZipFile(wordFile)
xml_content = document.read('word/document.xml')

wordObj = BeautifulSoup(xml_content.decode('utf-8'))
textStrings = wordObj.findAll("w:t")
for textElem in textStrings:
	closeTag = ""
	try:
		style = textElem.parent.previousSibling.find("w:pstyle")
		if style is not None and style["w:val"] == "Title":
			print("<h1>")
			closeTag = "</h1>"
	except AttributeError:
		# no tags to print
		pass
	print(textElem.text)
	print(closeTag)



