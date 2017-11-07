import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
}
response = requests.get('https://movie.douban.com/top250', headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
# print(soup.ol.li.div)
tags = soup.ol
for tag in tags:
    print(type(tag))
    print('------------')
with open('test.html', 'wb') as f:
    f.write(response.text.encode('utf-8'))
    f.close()
