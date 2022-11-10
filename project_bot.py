import telebot
import requests
from bs4 import BeautifulSoup
import os


def anek(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text)
    array = soup.find_all('div', {'class': "text"})
    for elem in range(len(array)):
        array[elem] = array[elem].text
    arr = []
    for i in range(len(array)):
        if 'читать дальше' not in array[i]:
            arr.append(array[i])
    return arr

def anek_new():
    url = 'https://www.anekdot.ru/release/anekdot/day/'
    last = 0
    for i in range(1,10000000):
        s = 'анекдот{}.txt'.format(i)
        if os.path.exists(s) == False:
            last = i
            break

    count = 0
    for i in range(1,len(anek(url))):
        try:
            s = 'анекдот' + str(i+last-1-count) +'.txt'
            s1 = 'анекдот' + str(i+last-1-count) + '_оценка.txt'
            print(s1)
            f = open(s, 'w')
            f.write(anek(url)[i-1])
            f.close()
            file = open(s1, 'w')
            file.write('0')
            file.close()
            print(i)
        except:
            count += 1

bot = telebot.TeleBot('5779219146:AAF9nHYsUGsRZ7xFXKK33L_A_NlaHBBCwpU')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Анекдот', 'Мем',  'Пост/метаирония')

keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.row('Избранные анекдоты', 'Новые анекдоты', 'Анекдот по id', 'Назад')

keyboard3 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard3.row('Избранные мемы', 'Новые мемы', 'Мем по id',  'Назад')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start, мы начинаем работу', reply_markup=keyboard1)


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Я memesbot. Я кидаю мемы, анекдоты и т.д. Существует предложка (просматривается человеком)')


@bot.message_handler(content_types=['text'])

def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Здарово, работяга')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'До побачення')
    elif message.text.lower() == 'анекдот':
        bot.send_message(message.chat.id, 'Выберите подпункт', reply_markup = keyboard2)
    elif message.text.lower() == 'мем':
        bot.send_message(message.chat.id, 'Выберите подпункт', reply_markup = keyboard3)
    elif message.text == 'Назад':
        bot.send_message(message.chat.id, 'Выберите тематику', reply_markup=keyboard1)

'''    elif message.text == 'Лучшие анекдоты':
        bot.send_message(message.chat.id, )
    elif message.text == 'Недавние анекдоты':
        bot.send_message(message.chat.id, )
    elif message.text == 'Лучшие мемы':
        bot.send_message(message.chat.id, )
    elif message.text == 'Недавние мемы':
        bot.send_message(message.chat.id, )
    elif message.text == 'За этот год':
        bot.send_message(message.chat.id, )
    else:
        bot.send_message(message.chat.id, 'Ничего не понял, но очень интересно')
'''
bot.polling()
