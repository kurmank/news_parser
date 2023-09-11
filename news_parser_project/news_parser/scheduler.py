from apscheduler.schedulers.background import BackgroundScheduler
from news_parser.news_parser import parse_and_save_news

def start():
    scheduler = BackgroundScheduler()
    # Запускаем задачу каждые 15 минут
    scheduler.add_job(parse_and_save_news, 'interval', minutes=15)
    
    scheduler.start()