# Generated by Django 3.2.6 on 2023-09-11 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_parser', '0002_auto_20230911_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
