import bs4
from selenium import webdriver #SELENIUM
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options #SELENIUM
from bs4 import BeautifulSoup as soup
import json

"""

Scraper:

to be used in a "main" type file (currently scrape_cli.py)

"""

class Scraper():

    ### SELENIUM SETUP ###

    DRIVER_PATH = "/usr/bin/chromedriver"



    ### MY ATTRIBUTES ###

    target_url = ""
    


    ### MAGIC METHODS ###

    def __init__(self, url_in="empty", is_headless=True):
        self.target_url = url_in
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
        '''
        if is_headless:
            options = Options()
            options.headless = True
            options.add_argument("--window-size=1920,1200")
            self.driver.options = options

            target_url = url_in
            self.driver.get(target_url)

        else:
            target_url = url_in
            self.driver.options = options
        '''



    ### TESTING ###

    def testing(self):
        print("Testing.")

    ### SELENIUM ###

    def headful(self, url_in):
        target_url = url_in
        
        return self.driver.get(target_url)

    def headless(self, url_in):
        # Use selenium.webdriver.chrome.options object to set the
        # driver to headless mode (You won't see the webpage as
        # the scraping happens)
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1200") 
        self.driver.options = options # gets set here

        # we just want the two lines of code from headful() anyway
        self.headful(url_in)


    ### BEAUTIFUL SOUP ###

    def soup_it(self, raw_html, mode): # TODO how do we want to do the modes?
        # html parsing
        page_soup = soup(raw_html, "html.parser")
        page_soup.prettify()
        ### vals_out = page_soup.findAll("td")

        return page_soup