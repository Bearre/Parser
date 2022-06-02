import requests
import random
from bs4 import BeautifulSoup as BS


UserAgents = [
    'Mozilla/5.0 (Linux; U) Opera 6.02 [en]',
    'Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 4.0) Opera 6.02 [en]',
    'Mozilla/4.0 (compatible; MSIE 5.0; Windows 95) Opera 6.02 [en]',
    'Mozilla/4.0 (compatible; MSIE 5.0; Windows 95) Opera 6.02 [de]',
    'Mozilla/4.0 (compatible; MSIE 5.0; Windows 2000) Opera 6.02 [en]',
    'Mozilla/4.0 (compatible; MSIE 5.0; Linux 2.4.20-686 i686) Opera 6.02 [en]',
    'Mozilla/4.0 (compatible; MSIE 5.0; Linux 2.4.18-4GB i686) Opera 6.02 [en]',
    'Opera/6.02 (Windows NT 4.0; U) [de]',
    'Opera/6.01 (X11; U; nn)',
    'Opera/6.01 (Windows XP; U) [de]',
    'Opera/6.01 (Windows 98; U) [en]',
    'Opera/6.01 (Windows 98; U) [de]',
    'Opera/6.01 (Windows 2000; U) [en]',
    'Opera/6.01 (Windows 2000; U) [de]',
    'Mozilla/5.0 (Windows 2000; U) Opera 6.01 [en]',
    'Mozilla/5.0 (Windows 2000; U) Opera 6.01 [de]',
    'Mozilla/4.78 (Windows 2000; U) Opera 6.01 [en]',
    'Mozilla/4.0 (compatible; MSIE 5.0; Windows XP) Opera 6.01 [it]',
    'Mozilla/4.0 (compatible; MSIE 5.0; Windows XP) Opera 6.01 [et]',
    'Mozilla/4.0 (compatible; MSIE 5.0; Windows XP) Opera 6.01 [de]',
    'Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 4.0) Opera 6.01 [en]',
    'Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 4.0) Opera 6.01 [de]',
    'Mozilla/4.0 (compatible; MSIE 5.0; Windows ME) Opera 6.01 [en]',
    'Mozilla/4.0 (compatible; MSIE 5.0; Windows ME) Opera 6.01 [de]',
    'Mozilla/4.0 (compatible; MSIE 5.0; Windows 98) Opera 6.01 [it]',
    'Mozilla/4.0 (compatible; MSIE 5.0; Windows 98) Opera 6.01 [fr]',
    'Mozilla/4.0 (compatible; MSIE 5.0; Windows 98) Opera 6.01 [en]',
    'Mozilla/4.0 (compatible; MSIE 5.0; Windows 98) Opera 6.01 [de]'
]
Proxies = [
    '203.30.191.202	80',
    '203.13.32.221	80',
    '203.24.102.56 80',
    '185.162.230.228 80',
    '203.23.104.37	80',
    '45.14.174.140	80',
    '173.245.49.118	80',
    '45.12.31.206	80',
    '172.67.254.148	80',
    '172.67.181.40	80'
]

URL = "https://coinmarketcap.com/ru/"

fake_user = random.choice(UserAgents)
fake_proxy = random.choice(Proxies)
# Проверка соединения
try:
    Request = requests.get(URL, headers={'User-Agent': fake_user}, proxies={'Proxy': fake_proxy})
    if Request.status_code:
        print(f'Successful connection to {URL}, code {Request.status_code}')
#    else:
#       print(f'Error code {Request.status_code}')
except Exception:
    Request = requests.get(URL, headers={'User-Agent': random.choice(UserAgents)})
    if Request.status_code:
        print('Successful connection!')
finally:
    pass


# Запись HTML в файл
# with open('test.html', 'w', encoding='UTF-8') as output_file:
#    output_file.write(Request.text)


a = []
# Получение HTML страницы
HTML = BS(Request.text, 'html.parser')
href = HTML.find('table', class_="h7vnx2-2").find_all('td')
for td in href:
    a.append(td.text)

for i in a:
    if i == '':
        a.remove(i)
    print(i, end='\n')
