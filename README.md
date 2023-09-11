"# news_parser" 

Парсер новостей на django с postgres.

## Требования

requirements.txt

## Установка

1. Склонируйте репозиторий:

   git clone https://github.com/kurmank/news_parser.git

2. Установите зависимости:
  pip install -r requirements.txt

3. Запустите миграции.
  python manage.py migrate
 
4. Запустите django-приложение и перейдите http://127.0.0.1:8000/admin.
   python manage.py runserver
5. login: admin
   password: 12345


P.S. Не разобрался, почему не работает докер.
