from bs4 import BeautifulSoup

from locators.quotes_page_locators import quotes_page_locators
from parsers.quote import quote_parser

class quote_page:
    def __init__(self,page):
        self.soup = BeautifulSoup(page,'html.parser')

    @property
    def quotes(self):
        locator = quotes_page_locators.quote
        quote_tags = self.soup.select(locator)
        return [quote_parser(e) for e in quote_tags]