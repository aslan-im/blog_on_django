from django.db import models
from django.contrib.auth.models import User
from django.utils.dateformat import format


class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        formatted_date = format(self.created_at, 'N j, Y, P')
        return self.title + ' | ' + str(self.author) + ' | ' + formatted_date
