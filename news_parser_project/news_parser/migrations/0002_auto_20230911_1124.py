# Generated by Django 3.1.13 on 2023-09-11 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_parser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='post_url',
            field=models.URLField(unique=True),
        ),
    ]
