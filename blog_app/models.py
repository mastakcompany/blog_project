from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название категории')
    slug = models.SlugField(unique=True)
    objects = models.Manager()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']

    def __str__(self):
        return f'Категория: {self.title}'


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок статьи')
    slug = models.SlugField(unique=True)
    content = models.TextField(verbose_name='Текст статьи')
    published = models.BooleanField(default=False, verbose_name='Статус публикации')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    views_count = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')
    objects = models.Manager()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Категория',
    )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']

    def increase_views_count(self):
        self.views_count += 1
        self.save()

    def __str__(self):
        return f'Статья: {self.title}'
