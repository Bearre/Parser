# Парсер рекомендаций сайта авито по основным категориям
# Без поддержки скроллинга по странице
# Добавить вывод результатов в файл
import random
import time
import requests
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
result = []  # Название : цена
categories = ['transport', 'nedvizhimost', 'rabota']  # Категории

for category in categories:
    fake_user = random.choice(UserAgents)
    proxy = random.choice(Proxies)

    URL = f"https://www.avito.ru/moskva/{category}"

    # Проверка соединения
    try:
        Request = requests.get(URL, headers={'User-Agent': fake_user}, proxies={'Proxy': proxy})
        if Request.status_code:
            print('Successful connection!')
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

    # Получение HTML страницы
    HTML = BS(Request.text, 'html.parser')

    # Парсинг
    href = HTML.find(class_='styles-root-vOrMe').find(class_='styles-list-M1e9B').find_all(class_='styles-item-W5Z4K')
    for div in href:
        try:
            title = div.find(class_='body-titleRow-AvL3d').find('a').text  # Название
            # source = div.find(class_='body-titleRow-AvL3d').find('a').get(href)  # Ссылка
        except Exception:
            print('Nothing found')
        try:
            price = div.find(class_='body-priceRow-h69TD').text.encode(encoding='ascii', errors='ignore')  # Цена
        except Exception:
            print('Nothing found')
        try:
            data = div.find(class_='text-text-LurtD').text
        except Exception:
            print('Nothing found')
        result.append([title, price, data])  # Переделать дату и источник

    time.sleep(10 + random.randint(0, 2))  # Выжидаем перед каждым новым запросом
print(result)
