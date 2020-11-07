#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cherrypy
import telebot
from config import token, chat_id, path_to_cert, url_server
from json_db import read_file


BOT_TOKEN = token
WEBHOOK_SSL_CERT = path_to_cert
Chat_id = chat_id
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def command_start(message):
    bot.send_message(message.chat.id, "Привет! Я price_bot")

@bot.message_handler(commands=["price"])
def command_price(message):
    load_price = read_file()
    price_12 = load_price['p_12']
    price_18 = load_price['p_18']
    bot.send_message(message.chat.id, f'На petshop\n за 12кг - {price_12}\n На petshop за 18кг - {price_18}')
    

def send_message(text, id=Chat_id):
    bot.send_message(id, text)

class WebhookServer(object):
    # index равнозначно /, т.к. отсутствию части после ip-адреса (грубо говоря)
    @cherrypy.expose
    def index(self):
        length = int(cherrypy.request.headers['content-length'])
        json_string = cherrypy.request.body.read(length).decode("utf-8")
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''

if __name__ == '__main__':

    bot.remove_webhook()
    bot.set_webhook(url=url_server,
                    certificate=open(WEBHOOK_SSL_CERT, 'r')) 
 
    cherrypy.config.update({
        'server.socket_host': '127.0.0.1',
        'server.socket_port': 7773,
        'engine.autoreload.on': False
    })
    cherrypy.quickstart(WebhookServer(), '/', {'/': {}})
