from bs4 import BeautifulSoup
from time import sleep
from parser_petshop import get_html
from price_bot import send_message
from parser_ozon import price_ozon_12, price_ozon_18
from parser_petshop import price_petshop_12, price_petshop_18
import requests



if __name__ == '__main__':
    price_ozon_12 = 0
    price_ozon_18
    price_petshop_12 = 0
    price_petshop_18
    while True:
        new_price_ozon_12 = price_ozon_12()
        new_price_ozon_18 = price_ozon_18()
        new_price_petshop_12 = price_petshop_12()
        new_price_petshop_18 = price_petshop_18()
        if new_price_ozon_12 != price_ozon_12:
            price_ozon_12 = new_price_ozon_12
            send_message(f'На озон за 12кг - {price_ozon_12}')
        if new_price_ozon_18 != price_ozon_18:
            price_ozon_18 = new_price_ozon_18
            send_message(f'На озон за 18кг - {price_ozon_18}')
        if new_price_petshop_12 != price_petshop_12:
            price_petshop_12 = new_price_petshop_12
            send_message(f'На petshop за 12кг - {price_petshop_12}')
        if new_price_petshop_18 != price_petshop_18:
            price_petshop_18 = new_price_petshop_18
            send_message(f'На petshop за 18кг - {price_petshop_18}')
        sleep(600)