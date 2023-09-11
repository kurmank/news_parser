from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler


class NewsParserConfig(AppConfig):
    name = 'news_parser'

    def ready(self):
        from . import scheduler
        scheduler.start()