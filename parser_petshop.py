from bs4 import BeautifulSoup
import requests
import re


url_petshop = 'https://www.petshop.ru/catalog/dogs/syxoi/vzroslye_1_6let/bessonovoy-dog-food-salmon-and-potato-bowl-lick/'
id_18 = 'offer-63133'
id_12 = 'offer-63132'
conditions_for_petshop = lambda tag: tag.name == 'span' and not tag.attrs


def get_html_as_text(url):
    '''sends a request Get to a given URL 
    and returns the received page as a string
    URL - string'''
    html = requests.get(url).text
    return html


def data_extraction_from_html_by_id(html_text, id): 
    soup = BeautifulSoup(html_text, features='lxml')
    try:
        return soup.find(attrs={'id': id})
    except TypeError:
        return None


def extraction_price_by_weight(filter, url, id):     
    soup = data_extraction_from_html_by_id(get_html_as_text(url), id)
    text = str(soup.findAll(filter))
    result = re.findall(r'\d.\d{3}', text)
    return result[0]


def mining_nunber(data_string): #перебирает по символьно строку и оставляет только цифры
    result = ''
    for char in data_string:
        if char.isdigit():
            result += char
    return int(result)

def receiving_price(filter, url, id):
    price_string = extraction_price_by_weight(filter, url, id)
    return mining_nunber(price_string)

def price_petshop_18():
    return receiving_price(conditions_for_petshop, url_petshop, id_18)

def price_petshop_12():
    return receiving_price(conditions_for_petshop, url_petshop, id_12)
