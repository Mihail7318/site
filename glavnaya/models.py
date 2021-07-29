from __future__ import unicode_literals
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from news.models import Post, Category
from faicon.fields import FAIconField
from mptt.models import MPTTModel, TreeForeignKey



class Slider(models.Model):

    STATUS_SLIDER = (
        ('Publish', 'Опубликовать'),
        ('Not_to_publish', 'Не публиковать'),
    )

    status = models.CharField(default='Publish', max_length=30, choices=STATUS_SLIDER, verbose_name='Статус')
    title = models.ForeignKey(Post,  related_name='Slidertitle', on_delete=models.CASCADE, verbose_name='Новость')
    image = models.ImageField(blank=True, upload_to='media/image/', null=True, verbose_name='Изображение')
    views = models.IntegerField(default=0, verbose_name='Количество просмотров', null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True)
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления', null=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Слайдер"
        verbose_name_plural = "Слайдеры"
        ordering = ['-created_at']



class Vidjet(models.Model):

    vidjetone = models.ForeignKey(Category, related_name='Vidjetone', on_delete=models.CASCADE, verbose_name='Виджет-1')
    vidjettwo = models.ForeignKey(Category, related_name='Vidjettwo', on_delete=models.CASCADE, verbose_name='Виджет-2')
    vidjetthree = models.ForeignKey(Category, related_name='Vidjetthree', on_delete=models.CASCADE, verbose_name='Виджет-3')


    def __int__(self):
        return self.id

    class Meta:
        verbose_name = 'Троица категории'
        verbose_name_plural = 'Троица категорий'



class Favorit(models.Model):

    favorit = models.ForeignKey(Category, related_name='favorit', on_delete=models.CASCADE, verbose_name='Ибранная категория')


    def __int__(self):
        return self.id

    class Meta:
        verbose_name = 'Ибранная категория'
        verbose_name_plural = 'Ибранная категория'


class Favorites(models.Model):

    favourites = models.ManyToManyField(Category, related_name='favourites', verbose_name='Список')

    def __int__(self):
        return self.id

    class Meta:
        verbose_name = 'Избранная категория'
        verbose_name_plural = 'Избранные категорий'




class Ikonki(models.Model):
    STATUS = (
        ('True', 'Опубликовать'),
        ('False', 'Не публиковать'),
    )
    title = models.CharField(max_length=30, verbose_name='Название')
    icon = FAIconField(verbose_name='Иконка')
    sylka = models.CharField(max_length=30, verbose_name='Сылка')
    status=models.CharField(max_length=10, choices=STATUS, verbose_name='Статус')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Социальные сети"
        verbose_name_plural = "Социальные сети"

class Menu(models.Model):

    title = models.CharField(max_length=30, verbose_name='Название')
    status = models.BooleanField(default=False, verbose_name='Использовать как главное меню')

    def __int__(self):
        return self.title

    class Meta:
        verbose_name = 'меню'
        verbose_name_plural = 'меню'

class Punct(MPTTModel):

    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', verbose_name='Родитель')
    punct = models.CharField(max_length=255, verbose_name='Название')
    slug = models.CharField(max_length=255, verbose_name='Ссылка')

    def __int__(self):
        return self.punct

    class Meta:
        verbose_name = 'Пункт'
        verbose_name_plural = 'Пункты'



class Footer(models.Model):
    vidjet_1 = models.TextField(max_length=255, verbose_name='Подвал')
    vidjet_2 = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name='Меню')
    vidjet_3 = RichTextUploadingField(blank=True, verbose_name='Контакты')

    def __int__(self):
        return self.id

    class Meta:
        verbose_name = 'Подвал'
        verbose_name_plural = 'Подвал'
