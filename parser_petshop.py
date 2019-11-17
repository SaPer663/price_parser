from bs4 import BeautifulSoup
#from time import sleep
#from price_bot import send_message
import requests
import re


url_petshop = 'https://www.petshop.ru/catalog/dogs/syxoi/vzroslye_1_6let/bessonovoy-dog-food-salmon-and-potato-bowl-lick/'
r_petshop = requests.get(url_petshop)
#attrs_petshop = {'class':'j_offer_price product-price'}

def get_html(url):
    html = requests.get(url).text
    return html


def data_extraction_from_html(possition): 
    
    soup = BeautifulSoup(get_html(url_petshop), features='lxml')
    text = str(soup.findAll(lambda tag: tag.name == 'span' and not tag.attrs ))
    result = re.findall(r'\d.\d{3}', text)
    return result[possition]


def mining_nunber(data_string): #перебирает по символьно строку и оставляет только цифры
    result = ''
    for char in data_string:
        if char.isdigit():
            result += char
    return int(result)

def receiving_price(possition):
    price_string = data_extraction_from_html(possition)
    price = mining_nunber(price_string)
    return price

def price_petshop_18():
    price = receiving_price(0)
    return price

def price_petshop_12():
    price = receiving_price(1)
    return price

