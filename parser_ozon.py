from bs4 import BeautifulSoup
from time import sleep
from parser_petshop import get_html, mining_nunber
import requests
import re



url_ozon = 'https://www.ozon.ru/context/detail/id/33471742/'
funtion = lambda tag: tag.name == 'span' and len(tag.attrs) == 2
                          
def data_extraction_from_html(func,url, possition):     
    soup = BeautifulSoup(get_html(url), features='lxml')
    text = str(soup.findAll(func))
    result = re.findall(r'\d.\d{3}', text)
    return result[possition]

def receiving_price(func, url, possition):
    price_string = data_extraction_from_html(func, url, possition)
    price = mining_nunber(price_string)
    return price


def price_ozon_18():
    price = receiving_price(funtion, url_ozon, 7)
    return price

def price_ozon_12():
    price = receiving_price(funtion, url_ozon, 6)
    return price
