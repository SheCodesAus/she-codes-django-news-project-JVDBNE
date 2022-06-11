from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    image = models.URLField(help_text='(Copy Image Address)', blank=True)

    class Meta: 
        ordering = ['-pub_date']