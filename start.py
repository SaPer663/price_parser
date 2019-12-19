from bs4 import BeautifulSoup
from time import sleep
from parser_petshop import get_html
from price_bot import send_message
from parser_ozon import price_ozon_12_18
from parser_petshop import price_petshop_12, price_petshop_18
from config import path
import requests
import json



if __name__ == '__main__':
    print('working')
    data_base_price = {}
    with open(path, 'r') as db:
        data_base_price = json.load(db)
    
    while True:
        check_db = str(data_base_price)
        new_price_ozon_12, new_price_ozon_18 = price_ozon_12_18(data_base_price['o_12'],\
                                                                data_base_price['o_18'])
        new_price_petshop_12 = price_petshop_12()
        new_price_petshop_18 = price_petshop_18()
        if new_price_ozon_12 != data_base_price['o_12']:
            data_base_price['o_12'] = new_price_ozon_12
            send_message(f"На озон за 12кг - {data_base_price['o_12']}")
        if new_price_ozon_18 != data_base_price['o_18']:
            data_base_price['o_18'] = new_price_ozon_18
            send_message(f"На озон за 18кг - {data_base_price['o_18']}")
        if new_price_petshop_12 != data_base_price['p_12']:
            data_base_price['p_12'] = new_price_petshop_12
            send_message(f"На petshop за 12кг - {data_base_price['p_12']}")
        if new_price_petshop_18 != data_base_price['p_18']:
            data_base_price['p_18'] = new_price_petshop_18
            send_message(f"На petshop за 18кг - {data_base_price['p_18']}")
        if check_db != str(data_base_price):
            with open(path, 'w') as db:
                json.dump(data_base_price, db)
        sleep(600)