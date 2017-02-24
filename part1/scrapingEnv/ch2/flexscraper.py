from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import random

#Retrieves a list of all internal links found on a page
def getInternalLinks(bsObj, includeUrl):
	internalLinks = []

	#finds all links that begin with a "/"
	for link in bsObj.findAll("a",href=re.compile("^(\/|.*(http:\/\/"+includeUrl+")).*")): #find 'a' internal link
		if link.attrs['href'] is not None: #if the link is not None 
			if link.attrs['href'] not in internalLinks: #if the link is new
				internalLinks.append(link.attrs['href']) #add to list of links
	return internalLinks

#Retrieves a list of all external links found on a page
def getExternalLinks(bsObj, url):
	excludeUrl = getDomain(url)
	externalLinks = []

	#finds all links that start with 'http' or 'www' that do not contain the current URL
	for link in bsObj.findAll("a",href=re.compile("^(http)((?!"+excludeUrl+").)*$")): #find 'a' external link
		if link.attrs['href'] is not None and len(link.attrs['href']) != 0: #if the link is not None or 0
			if link.attrs['href'] not in externalLinks: #if the link is new
				externalLinks.append(link.attrs['href'])
	return externalLinks

def getDomain(address):
	return urlparse(address).netloc

def followExternalOnly(bsObj, url):
	externalLinks = getExternalLinks(bsObj, url) #get the page's external links
	if len(externalLinks) == 0: #if no external links
		print("Only internal links here. Try again.")
		internalLinks = getInternalLinks(bsObj, getDomain(url)) #instead, look at internal links
		randInternalLink = "http://"+getDomain(url)
		randInternalLink += internalLinks[random.randint(0, len(externalLinks)-1)] #get random internal link
		bsObj = BeautifulSoup(urlopen(randInternalLink)) #create new beautifulsoup object
		
		#try again
		followExternalOnly(bsObj, randInternalLink) #recursively call with new elements

	else:
		randomExternal = externalLinks[random.randint(0, len(externalLinks)-1)] #get random external link
		try:
			nextBsObj = BeautifulSoup(urlopen(randomExternal)) #create new beautifulcoup object
			print(randomExternal)
			#next page!
			followExternalOnly(nextBsObj, randomExternal) #recursively call with new elements
		except HTTPError:
			#try again
			print("Encountered error at "+randomExternal+"! Trying again")
			followExternalOnly(bsObj, url) #recursively calling again

url = "http://oreilly.com"
bsObj = BeautifulSoup(urlopen(url))

followExternalOnly(bsObj,url) #recursively follow external links




# SECOND EXAMPLE: GETTING ALL INTERNAL / EXTERNAL LINKS ON A SINGLE PAGE FIRST
# ~ doesn't work?

# #Collects a list of all external URLs found on the site
# allExtLinks = set()
# allIntLinks = set()
# def getAllExternalLinks(siteUrl):
# 	html = urlopen(siteUrl)
# 	bsObj = BeautifulSoup(html)
# 	internalLinks = getInternalLinks(bsObj, splitAddress(siteUrl)[0])
# 	externalLinks = getExternalLinks(bsObj, splitAddress(siteUrl)[0])
# 	for link in externalLinks:
# 		if link not in allExtLinks:
# 			allExtLinks.add(link)
# 			print(link)
# 	for link in internalLinks:
# 		if link not in allExtLinks:
# 			print("about to get link: "+link)
# 			allIntLinks.add(link)
# 			getAllExternalLinks("http://"+getDomain(siteUrl)+link)

# getAllExternalLinks("http://oreilly.com")

