import requests
from bs4 import BeautifulSoup
from time import sleep
from price_bot import send_message
from parser_ozon import price_petshop_12_18
from config import path
from json_db import read_file, write_file



if __name__ == '__main__':
    print('working')
    data_base_price = {}
    data_base_price = read_file()
    
    while True:
        if isinstance(data_base_price, dict):
            check_db = str(data_base_price)
            new_price_petshop_12, new_price_petshop_18 = price_petshop_12_18()
            
            if new_price_petshop_12 != data_base_price['p_12']:
                data_base_price['p_12'] = new_price_petshop_12
                send_message(f"На petshop за 12кг - {data_base_price['p_12']}")
            if new_price_petshop_18 != data_base_price['p_18']:
                data_base_price['p_18'] = new_price_petshop_18
                send_message(f"На petshop за 18кг - {data_base_price['p_18']}")
            if check_db != str(data_base_price):
                write_file(data_base_price)
        else:
            send_message(f'У нас ошибка {data_base_price}')
        sleep(600)