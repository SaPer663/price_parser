import requests
import re
import json
from bs4 import BeautifulSoup
from time import sleep
from config import url_ozon, url_ozon_of_get_json, url_petshop, url_petshop_of_get_json


def get_json_from_server(url_base, url_json):
    try:
        s = requests.Session()
        s.get(url_base)
        sleep(2)
        return s.get(url_json).json()
    except Exception as ex:
        return ex


def price_ozon_12_18():
    result = [0, 0]
    json_input = get_json_from_server(url_ozon, url_ozon_of_get_json)
    list_prices_and_titles = json_input['pdp']['product']['product-220660-default-1']\
                                       ['readyAspects']['regular']['regularVariants']\
                                       [1]['aspectVariants']
    for price in list_prices_and_titles:
        if int(price['name']) == 12000 and price['available']:
            result[0] = price['price']['totalPrice']
        if int(price['name']) == 18000 and price['available']:
            result[1] = price['price']['totalPrice']

    return result

def price_petshop_12_18():
    result = {'price_12': 0, 'price_18': 0}
    list_prices_and_titles = get_json_from_server(url_petshop, url_petshop_of_get_json)
    if isinstance(list_prices_and_titles, list):
        for price in list_prices_and_titles:
            if int(price['Size']) == 12000:
                if price['IsAvailable']:
                    result['price_12'] = price['Price']
                else:
                    result['price_12'] = -1
            if int(price['Size']) == 18000:
                if price['IsAvailable']:
                    result['price_18'] = price['Price']
                else:
                    result['price_18'] = -1
        return result.values()
    else:
        return list_prices_and_titles