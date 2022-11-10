import requests
from bs4 import BeautifulSoup
import copy
import os

url = 'https://www.anekdot.ru/release/anekdot/day/'
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