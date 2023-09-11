from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import News


# Register your models here.

#admin.site.register(News)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'date_create', 'generate_json_link')

    def generate_json_link(self, obj):
        url = reverse('generate_json') + f'?news_ids[]={obj.id}'
        return format_html('<a href="{}" target="_blank">Generate JSON</a>', url)

    generate_json_link.short_description = 'Generate JSON'

