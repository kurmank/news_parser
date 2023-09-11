import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from  .models import News
import json
import hashlib
#from django.utils import timezone
import time
import datetime

def parse_and_save_news():
    #Получаем код динамичной страницы с помощью Selenium
    # Инициализация браузера
    driver = webdriver.Chrome()
    
    url = 'https://78.ru/news'
    # Открываем страницу
    driver.get(url)

    # Дожидаемся загрузки контента 
    time.sleep(1)  # Пример ожидания в 5 секунд

    # Получаем HTML-код страницы
    page_source = driver.page_source
   
    # Закрываем веб-драйвер
    driver.quit()

    #Получаем ссылки на новости с помощью BS
    soup = BeautifulSoup(page_source, 'html.parser')
    news_links = soup.find_all('a', class_='link link_black news-feed-timeline-item news-feed-timeline-item_rose')

    for link in news_links:
        news_url = 'https://78.ru' + link['href']
        #проводим проверкуы
        if not News.objects.filter(post_url=news_url).exists():
            news_text = get_news_text(news_url)
        else:
            # Новость уже существует в базе данных, пропускаем парсинг
            print(f"Новость уже существует: {news_url}")
        
        

# Функция для получения текста и атрибутов новости
def get_news_text(url):
    # Инициализация браузера
    driver = webdriver.Chrome()
    
    # Открываем страницу
    driver.get(url)

    # Дожидаемся загрузки контента 
    time.sleep(1)  # Пример ожидания в 5 секунд

    # Получаем HTML-код страницы
    page_source_article = driver.page_source
    
    # Закрываем веб-драйвер
    driver.quit()

    # Получаем необходимую информацию (заголовок, дату, текст и т.д.)
    bs = BeautifulSoup(page_source_article, 'html.parser')
    post_url = url
    post_title = bs.find('title').text
    post_text = str(bs.find('div', class_='publication__body'))+str(bs.find('div', class_='view-img view-img_border-rose'))
    post_id = hashlib.md5(post_url.encode()).hexdigest()
    
    #парсим json на дату
    data_to_json = bs.find('script', type ='application/ld+json').text
    data_to_json = json.loads(data_to_json)
    date_create = data_to_json['datePublished']
    date_create = datetime.datetime.strptime(date_create, '%Y-%m-%dT%H:%M:%S.%fZ')
    

    #сохраняем в бд
    news = News(
            post_url=post_url,
            post_title=post_title,
            date_create=date_create,
            post_text=post_text,
            post_id=post_id,
        )
    news.save()

    # Сохранение данных в JSON файл
    news_data = {
        "post__url": post_url,
        "post__title": post_title,
        "date__create": date_create.timestamp(),
        "post__text": post_text,
        "post__id": post_id,
    }
    filename = f"78ru_{date_create.strftime('%Y-%m-%d_%H:%M')}.json"
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(news_data, json_file, ensure_ascii=False, indent=4)
