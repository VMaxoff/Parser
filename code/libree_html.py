from bs4 import BeautifulSoup
from requests import get
a = get('http://books.toscrape.com/catalogue/category/books/classics_6/index.html')

soup = BeautifulSoup(a.text, "lxml")

def prices():
    for i in soup.find_all('p', {'class':'price_color'}):
        yield i.text

def names():
    for i in soup.find_all('h3'):
        yield i.text
