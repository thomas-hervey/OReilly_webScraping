from selenium import webdriver

import requests
from bs4 import BeautifulSoup

#getting cookies
driver = webdriver.PhantomJS(executable_path='')
driver.get("http://pythonscraping.com")
driver.implicitly_wait(1)
print(driver.get_cookies())

#setting beaders
session = requests.Session()
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
           "Accept:":"text/html,application/xhtml+xml,application/xml;q=0.9,imag,webp,*/*;q=0.8"}
url = "https://www.whatsmybrowser.com/developers/what-http-headers-is-my-browser-sending"
req = session.get(url, headers = headers)

bsObj = BeautifulSoup(req.text)
print(bsObj.find("table",{"class":"table-striped"}).get_text)
