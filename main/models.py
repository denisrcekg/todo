from django.db import models


class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class Book(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    price = models.IntegerField()
    genre = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    year = models.DateField()
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=0)
