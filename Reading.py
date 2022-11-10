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


url = 'https://vk.com/wall-125980899?own=1'

def postironya(url='https://vk.com/wall-125980899?own=1'):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text)
    array = []
    div = soup.find_all('a')
    for a in div:
      array.append(a.get('style'))
    arr = []
    for i in range(len(array)):
      if array[i]!= None and array[i] != '' and array[i] != 'display: none' :
        arr.append(array[i])
    t = []
    for i in range(len(arr)):
      if ''.join([arr[i][0], arr[i][1], arr[i][2]]) == 'wid':
        t.append(arr[i])
    tmp = []
    for i in range(len(t)):
      px1 = t[i].find('px')
      px2 = t[i].rfind('px')
      s = ''.join([t[i][px1-3], t[i][px1-2], t[i][px1-1]])
      s1 = ''.join([t[i][px2-3], t[i][px2-2], t[i][px2-1]])
      if int(s)>300 and int(s1)>300:
        tmp.append(t[i])
      tmp1 = []
    for i in range(len(tmp)):
      k = tmp[i].find('http')
      tmp1.append(tmp[i][k:-2:])
    return tmp1

print(postironya())
bot.send_photo(ид_получателя, 'tmp[i]')