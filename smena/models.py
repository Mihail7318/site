from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.conf import settings

from news.models import Category, Post

# Create your models here.


class Smena(models.Model):

    STATUS_NEWS = (
        ('Publish', 'Опубликовать'),
        ('Not_to_publish', 'Не публиковать'),
    )

    status = models.CharField(default='Publish',max_length=30, choices=STATUS_NEWS, verbose_name='Статус')
    yved = models.BooleanField(default=False, verbose_name='Уведомить')
    title = models.CharField(max_length=255, db_index=True, verbose_name='Наименование')
    slug = models.SlugField(unique=True, verbose_name='Ссылка')
    rubric = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Рубрика')
    content = RichTextUploadingField(blank=True, verbose_name='Описание')
    image = models.ImageField(blank=True, upload_to='media/image/', null=True, verbose_name='Изображение')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Приподователь')
    news = models.ManyToManyField(Post, verbose_name='новости')
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('postsmena', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Cмена'
        verbose_name_plural = 'Cмены'
        ordering = ['-created_at']


