import requests
from pages.quotes_page import quote_page

page_content = requests.get('http://quotes.toscrape.com').content
page = quote_page(page_content) 

for quote in page.quotes:
    print(quote)