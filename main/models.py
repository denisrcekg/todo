from django.db import models
from datetime import datetime


class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class ToDo(models.Model):
    text = models.CharField(max_length=100, verbose_name='Задача')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    is_closed = models.BooleanField(default=False, verbose_name='Выполнена')
    is_favorite = models.BooleanField(default=False, verbose_name='Избранная')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

#BookStore
class BookStore(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    subtitle = models.CharField(max_length=100, verbose_name='Подзаголовок')
    description = models.CharField(max_length=700, verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    genre = models.CharField(max_length=60, verbose_name='Жанр')
    author = models.CharField(max_length=35, verbose_name='Автор')
    is_favorite = models.BooleanField(default=False, verbose_name='Избранная')
    year = models.DateTimeField(verbose_name='Год издания')
    date = models.DateField(auto_now_add=True, verbose_name='Добавление книги на сайт')

    class Meta:
        verbose_name = 'Книжный магазин'
        verbose_name_plural = 'Книжные магазины'