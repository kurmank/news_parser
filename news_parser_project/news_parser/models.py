from django.db import models

# Create your models here.

class News(models.Model):
    id = models.AutoField(primary_key=True)
    post_url = models.URLField(unique=True)
    post_title = models.CharField(max_length=255)
    date_create = models.DateTimeField()
    post_text = models.TextField()
    post_id = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.post_title


