from bs4 import BeautifulSoup
from locators.all_books_page import all_books_page_locator
from parsers.book_parser import BookParser
class all_books_page:
    def __init__(self,page_content):
         self.soup = BeautifulSoup(page_content,'html.parser')

    @property
    def books(self):
         return [BookParser(e) for e in self.soup.select(all_books_page_locator.books)]