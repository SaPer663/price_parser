from bs4 import BeautifulSoup
from time import sleep
from config import url_ozon, url_ozon_of_get_json
import requests
import re
import json


def data_extraction_from_server():     
    s = requests.Session()
    s.get(url_ozon)   
    sleep(2)
    return s.get(url_ozon_of_get_json).text


def price_ozon_12_18(price_12, price_18):
    result = [price_12, price_18]
    json_input = json.loads(data_extraction_from_server())
    list_prices_and_titles = json_input['pdp']['product']['product-220660-default-1']\
                                       ['readyAspects']['regular']['regularVariants']\
                                       [1]['aspectVariants']
    for price in list_prices_and_titles:
        if int(price['name']) == 12000 and price['available']:
            result[0] = price['price']['totalPrice']
        if int(price['name']) == 18000 and price['available']:
            result[1] = price['price']['totalPrice']

    return result
    