import json
from django.http import JsonResponse
from .models import News

def generate_json(request):
    selected_news_ids = request.GET.getlist('news_ids[]')
    selected_news = News.objects.filter(pk__in=selected_news_ids)

    data = []
    for news in selected_news:
        news_data = {
            "post__url": news.post_url,
            "post__title": news.post_title,
            "date__create": news.date_create.timestamp(),
            "post__text": news.post_text,
            "post__id": news.post_id,
        }
        data.append(news_data)

    response_data = {
        'news': data
    }
    return JsonResponse(response_data)
