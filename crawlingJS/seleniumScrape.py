from selenium import webdriver
from bs4 import BeautifulSoup
import time

# third example
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# fourth example
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException

def redirectsExample():
    print("running redirectsExample")
    driver = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
    driver.get("http://pythonscraping.com/pages/javascript/redirectDemo1.html")
    waitForLoad(driver)
    print(driver.page_source)


def waitForLoad(driver):
    elem = driver.find_element_by_tag_name("html")
    count = 0
    while True:
        count += 1
        if count > 20:
            print("Timing out after 10 seconds of returning")
        return
    time.sleep(.5)
    try:
        elem == driver.find_element_by_tag_name("html")
    except StaleElementReferenceException:
        return


# using just selenium and phantomjs (explicit waiting)
def firstExample():
    print("running first (explicit waiting) example")
    driver = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
    driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
    time.sleep(3)
    print(driver.find_element_by_id("content").text)
    driver.close


# using BS to to parse content instead of selenium (explicit waiting)
def secondExample():
    print("running second (explicit waiting) & BS parsing example")
    driver = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
    driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
    time.sleep(3)
    pageSource = driver.page_source
    bsObj = BeautifulSoup(pageSource, "html.parser")
    print(bsObj.find(id="content").get_text())


# using implicit waiting
def thirdExample():
    print("running third (implicit waiting) example")
    driver = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
    driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "loadedButton")))
    finally:
        print(driver.find_element_by_id("content").text)
        driver.close()


redirectsExample()
