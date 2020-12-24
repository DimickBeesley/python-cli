import argparse
from Scraper import Scraper

"""
Web-Scraping cli tool powered by selenium for flexibility:

I want to be able to either fetch one page or a type(s) of 
<tag(s)> from multiple pages depending on.


Original Purpose:
the sts project needed to have data scraped from links that
held card and relic data, but this could come in handy in 
future projects, so I'm making it flexible.

Card link: https://slay-the-spire.fandom.com/wiki/Category:Cards
Relic link: https://slay-the-spire.fandom.com/wiki/Relics
"""

### ARGPARSE SETUP ###

parser = argparse.ArgumentParser()
parser.add_argument('--input')



if __name__ == "__main__":
    scr = Scraper()
    scr.headless("https://www.google.com")
