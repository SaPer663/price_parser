from bs4 import BeautifulSoup
from time import sleep
from parser_petshop import get_html
import requests



url_ozon = 'https://www.ozon.ru/context/detail/id/33471742/'
url_ozon_12 = 'https://www.ozon.ru/context/detail/id/33471728/'
r_ozon = requests.get(url_ozon)
r_ozon_12 = requests.get(url_ozon_12)

attrs_ozon = {'class':'a4l1'}
                          

def data_extraction_from_html(url, dict_attr): 
    soup = BeautifulSoup(get_html(url), features='lxml')
    try:
        return soup.find(attrs=dict_attr)
    except TypeError:
        return None


def mining_nunber(data_string): #перебирает по символьно строку и оставляет только цифры
    result = ''
    for char in data_string:
        if char.isdigit():
            result += char
    return int(result)

def receiving_price(request_objc, attr):
    html_text = data_extraction_from_html(request_objc.text, attr)
    price = mining_nunber(html_text.get_text())
    return price

def price_ozon_18():
    price = receiving_price(r_ozon, attrs_ozon)
    return price

def price_ozon_12():
    price = receiving_price(r_ozon_12, attrs_ozon)
    return price

