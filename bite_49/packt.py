from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

PACKT = 'https://bites-data.s3.us-east-2.amazonaws.com/packt.html'
CONTENT = requests.get(PACKT).text

Book = namedtuple('Book', 'title description image link')


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    
    soup = Soup(CONTENT, 'html.parser')
    book_div = soup.find('div', class_='dotd-main-book')

    title = book_div.find('h2').text.strip()
    description_div = soup.find('div', class_='dotd-main-book-summary').find_all('div')[2]
    description = description_div.text.strip()
    image = book_div.find('img')['src']
    link = book_div.find('a')['href']
    
    return Book(title, description, image, link)