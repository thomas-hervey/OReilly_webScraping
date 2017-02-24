from urllib.request import urlopen
from bs4 import BeautifulSoup
import unittest

class TestWikipedia(unittest.TestCase):
    bsObj = None
    url = None

    def test_PageProperties(self):
        global bsObj
        global url
        url = "http://en.wikipedia.org/wiki/Monty_Python"

        # test first 100 pages we find
        for i in range(1,100):
            bsObj = bsObj = BeautifulSoup(urlopen(url), "html.parser")
            titles = self.titleMatchesURL()
            self.assertEquals(title[0], titles[1])
            self.assertTrue(self.contentExists())
            url = self.getNextLink()
        print("done!")

    def titleMatchesURL(self):
        global bsObj
        global url
        pageTitle = bsObj.find("h1").get_text()
        urlTitle = url[(url.index("/wiki/")+6):]
        urlTitle = urlTitle.replace("_", " ")
        urlTitle = unquote(urlTitle)
        return [pageTitle.lower(), urlTitle.lower()]

    def contentExists(self):
        global bsObj
        classontent = bsObj.find("div", {"id":"mw-content-text"})
        if content is not None:
            return True
        return False

    def getNextLink(self):
        pass
        #return random link on page

    # def setUpClass():
    #     global bsObj
    #     url = "http://en.wikipedia.org/wiki/Monty_Python"
    #     bsObj = BeautifulSoup(urlopen(url), "html.parser")
    #
    # def test_titleText(self):
    #     global bsObj
    #     pageTitle = bsObj.find("h1").get_text()
    #     self.assertEqual("Monty Python", pageTitle)
    #
    # def test_contentExists(self):
    #     global bsObj
    #     content = bsObj.find("div", {"id":"mw-content-text"})
    #     self.assertIsNotNone(content)

if __name__ == '__main__':
    unittest.main()
