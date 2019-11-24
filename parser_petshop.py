from bs4 import BeautifulSoup
import requests
import re


url_petshop = 'https://www.petshop.ru/catalog/dogs/syxoi/vzroslye_1_6let/bessonovoy-dog-food-salmon-and-potato-bowl-lick/'
id_18 = 'offer-63133'
id_12 = 'offer-63132'
conditions_for_petshop = lambda tag: tag.name == 'span' and not tag.attrs


def get_html(url):
    html = requests.get(url).text
    return html


def data_extraction_from_html_by_id(html_doc, id): 
    soup = BeautifulSoup(html_doc, features='lxml')
    try:
        return soup.find(attrs={'id': id})
    except TypeError:
        return None


def extraction_price_by_weight(func, url, id):     
    soup = data_extraction_from_html_by_id(get_html(url), id)
    text = str(soup.findAll(func))
    result = re.findall(r'\d.\d{3}', text)
    return result[0]


def mining_nunber(data_string): #перебирает по символьно строку и оставляет только цифры
    result = ''
    for char in data_string:
        if char.isdigit():
            result += char
    return int(result)

def receiving_price(func, url, id):
    price_string = extraction_price_by_weight(func, url, id)
    price = mining_nunber(price_string)
    return price

def price_petshop_18():
    price = receiving_price(conditions_for_petshop, url_petshop, id_18)
    return price

def price_petshop_12():
    price = receiving_price(conditions_for_petshop, url_petshop, id_12)
    return price
