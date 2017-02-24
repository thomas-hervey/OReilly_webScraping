# # download single file
# from urllib.request import urlretrieve, urlopen
# from bs4 import BeautifulSoup

# html = urlopen("http://www.pythonscraping.com")
# bsObj = BeautifulSoup(html)
# imageLocation = bsObj.find("a", {"id": "logo"}).find("img")["src"]
# urlretrieve (imageLocation, "logo.jpg")




# # download all internal files
# import os
# from urllib.request import urlretrieve, urlopen
# from bs4 import BeautifulSoup

# downloadDirectory = "downloaded"
# baseUrl = "http://pythonscraping.com"

# def getAbsoluteUrl(baseUrl, source):
# 	if source.startswith("http://www."):
# 		url = "http://"+source[11:]
# 	elif source.startswith("http://"):
# 		url = source
# 	elif source.startswith("www."):
# 		url = source[4:]
# 		url = "http://"+source
# 	else:
# 		url = baseUrl+"/"+source

# 	if baseUrl not in url:
# 		return None
# 	return url

# def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
# 	path = absoluteUrl.replace("www.","")
# 	path = path.replace(baseUrl,"")
# 	path = downloadDirectory+path
# 	directory = os.path.dirname(path)

# 	if not os.path.exists(directory):
# 		os.makedirs(directory)

# 	return path


# html = urlopen("http://www.pythonscraping.com")
# bsObj = BeautifulSoup(html)
# downloadList = bsObj.findAll(src=True)

# for download in downloadList:
# 	fileUrl = getAbsoluteUrl(baseUrl, download["src"])
# 	if fileUrl is not None:
# 		print(fileUrl)

# urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))



# # basic CSV downloading
# import csv

# csvFile = open("test.csv", 'w+')
# try:
# 	writer = csv.writer(csvFile)
# 	writer.writerow(('number', 'number plus 2', 'number times 2'))
# 	for i in range(10):
# 		writer.writerow( (i,i+2,i*2))
# finally:
# 	csvFile.close()




# # beautiful soup table reading
# import csv
# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
# bsObj = BeautifulSoup(html)

# #the main comparison table is currently the first table on the page
# table = bsObj.findAll("table",{"class":"wikitable"})[0]
# rows = table.findAll("tr")
# csvFile = open("editors.csv","wt")
# writer = csv.writer(csvFile)
# try:
# 	for row in rows:
# 		csvRow = []
# 		for cell in row.findAll(['td', 'th']):
# 			csvRow.append(cell.get_text())
# 			writer.writerow(csvRow)
# finally:
# 	csvFile.close()




# mySQL example (NOT WORKING? COME BACK TO THIS!!!)
import pymysql
conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock',user='root',passwd='MQZ(mp1100',db='mysql')
cur = conn.cursor()
cur.execute("USE scraping")
cur.execute("SELECT * FROM pages WHERE id=1")
print(cur.fetchone())
cur.close()
conn.close()



