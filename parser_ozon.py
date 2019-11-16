from bs4 import BeautifulSoup
from time import sleep
import requests
import cherrypy
import telebot


url = 'https://www.ozon.ru/context/detail/id/33471742/'
r = requests.get(url)

def data_extraction_from_html(html_doc): 
    soup = BeautifulSoup(html_doc, features='lxml')
    try:
        return soup.find(attrs={'class':'a4l1'})
    except TypeError:
        return None


def mining_nunber(data_string):#перебирает по символьно строку и оставляет только цифры
    result = ''
    for char in data_string:
        if char.isdigit():
            result += char
    return int(result)

def receiving_price():
    html_text = data_extraction_from_html(r.text)
    price = mining_nunber(html_text.get_text())
    return price

price = 0
while True:
    new_price = receiving_price()
    if new_price != price:
        price = new_price
        print(price)
        continue
    sleep(30)
    print(30)
