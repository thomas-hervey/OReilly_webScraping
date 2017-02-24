import time
from urllib.request import urlretrieve
import subprocess
from selenium import webdriver

# create new selenium driver
driver = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
driver = webdriver.Firefox()
driver.get("http://amazon.com/War-Peace-Leo-Nikolayevich-Tolstoy/dp/1427030200")
time.sleep(2)

# click on the book preview button
driver.find_element_by_id("sitbLogoImg").click()
imageList = set()

# wait for the page to load
time.sleep(5)

# while the right arrow is available for clicking, turn through pages
while "pointer" in driver.find_element_by_id("sitbReaderRightPageTurner").get_attribute("style"):
    driver.find_element_by_id("sitbReaderRightPageTurner").click()
    time.sleep(2)

    # get any new pages that have loaded (multiple pages can load at once, but duplicates will not be added to set)
    pages = driver.find_elements_by_xpath("//div[@class='pageImage']/div/img")
    for page in pages:
        image = page.get_attribute("src")
        imageList.add(image)
driver.quit()

# start processing the images we've collected URLs for with Tesseract
for image in sorted(imageList):
    urlretrieve(image, "page.jpg")
    p = subprocess.Popen(["tesseract", "page.jpg", "page"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    f = open("page.txt", "r")
    print(f.read())
