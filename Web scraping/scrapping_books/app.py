import requests
from pages.all_books_page import all_books_page

page_content = requests.get('http://books.toscrape.com').content
page = all_books_page(page_content)

books = page.books
for book in books:
    print(books)

