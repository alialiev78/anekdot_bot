import telebot
import requests
from bs4 import BeautifulSoup
import os
import random


def random_number(first, last, n):
    tmp = []
    while len(tmp) != n:
        g = random.randint(first, last)
        if g not in tmp:
            tmp.append(g)
    return tmp


lupa = random_number(1, 15, 3)
for i in range(len(tmp)):
    s = 'постирония' + str(i) + '.jpg'
    with open(s, 'rb') as f:
        bot.sendphoto(update.message.chat_id, f)
