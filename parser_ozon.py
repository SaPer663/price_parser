from bs4 import BeautifulSoup
from time import sleep
from parser_petshop import get_html, data_extraction_from_html, receiving_price, mining_nunber
import requests
import re



url_ozon = 'https://www.ozon.ru/context/detail/id/33471742/'
funtion = lambda tag: tag.name == 'span' and len(tag.attrs) == 2
                          

def price_ozon_18():
    price = receiving_price(funtion, url_ozon, 7)
    return price

def price_ozon_12():
    price = receiving_price(funtion, url_ozon, 6)
    return price

