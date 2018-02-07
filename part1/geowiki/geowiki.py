import urllib3
import certifi
http = urllib3.PoolManager(
	cert_reqs='CERT_REQUIRED',
	ca_certs=certifi.where()
)

from bs4 import BeautifulSoup
import datetime
import random
import re

# NOT QUITE WORKING

random.seed(datetime.datetime.now())

def getLinks(articleUrl):
	html = http.request('GET', "http://en.wikipedia.org"+articleUrl)
	bsObj = BeautifulSoup(html, "lxml")
	return bsObj.find("div", {"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))

def getHistoryIPs(pageUrl):
	pageUrl = pageUrl.replace("/wiki/", "")
	historyUrl = "http://en.wikipedia.org/w/index.php?title="+pageUrl+"&action=history"
	print("history url is: "+historyUrl)
	html = http.request(historyUrl)
	bsObj = BeautifulSoup(html, "lxml")

	#finds only the links with class "mw-anonuserlink" which has IP adress instead of username
	ipAddresses = bsObj.findAll("a", {"class":"mw-anonuserlink"})
	addressList = set()
	for ipAddress in ipAddresses:
		addressList.add(ipAddress.get_text())
	return addressList

def getCountry(ipAddress):
	try:
		response = http.request("http://fregeoip.net/json/"+ipAddress).read().decode('utf-8')
	except error:
		return None
	responseJSON = json.loads(response)
	return responseJSON.get("country_code")


links = getLinks("/wiki/Python_(programming_language)")

while(len(links) > 0):
	for link in links:
		print("-----------")
		historyIPs = getHistoryIPs(link.attrs["href"])
		for historyIP in historyIPs:
			country = getCountry(historyIP)
			if country is not None:
				print(historyIP+" is from "+country)

	newLink = links[random.randint(0, len(links)-1)].attrs["href"]
	links = getLinks(newLink)
