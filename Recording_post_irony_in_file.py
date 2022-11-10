import requests
from bs4 import BeautifulSoup


def postironya(url):
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


count = 0

images_urls = []
for i in range(100, 850): #750
  try:
    s = 'https://vk.com/wall-125980899?offset={}&own=1'.format(20*(i-1))
    print(i)
    images_urls.extend(postironya(s))
  except:
    pass
#print(images_urls)
print(len(images_urls))


for i in range(len(images_urls)):
    try:
        r = requests.get(images_urls[i], stream = True)
        k = 'постирония{}.jpg'.format(i+1-count)
        k1 = 'постирония{}.txt'.format(i+1-count)
        print(k1)
        f1 = open(k1, 'w')
        f1.write('0')
        f1.close()
        with open(k, 'bw') as f:
            for chunk in r.iter_content(8192):
                f.write(chunk)
    except:
        count += 1