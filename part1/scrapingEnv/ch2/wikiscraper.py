from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re


#random.seed(datetime.datetime.now())

pages = set()
def getLinks(artileUrl):
	global pages
	html = urlopen("http://en.wikipedia.org" + artileUrl)
	bsObj = BeautifulSoup(html, "html.parser")

	try:
		print(bsObj.h1.get_text()) #print first header text
		print(bsObj.find(id="mw-content-text").findAll("p")[0]) #find first paragraph of text
		print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href']) #find 'edit page' links
	except:
		print("This page is missing something! No worries though!")

	for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
		if 'href' in link.attrs:
			if link.attrs['href'] not in pages:
				#we have encountered a new page
				newPage = link.attrs['href']
				print("-----------------\n"+newPage)
				pages.add(newPage)
				getLinks(newPage)

getLinks("")

# 	return bsObj.find("div", {"id":"bodyContent"})\
# 				.findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))

# links = getLinks("/wiki/Kevin_Bacon") #start article

# while len(links) > 0: #if there are links to be observed
# 	newArticle = links[random.randint(0,len(links)-1)].attrs["href"] #find new random article on that page
# 	print(newArticle)
# 	links = getLinks(newArticle) #get the articles within the new random article