from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse



class Sovet(models.Model):

    title = models.CharField(max_length=255, db_index=True, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='Ссылка')
    content = RichTextUploadingField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('get_one_board_of_trustees', kwargs={"slug": self.slug})


    class Meta:
        verbose_name = 'Cовет'
        verbose_name_plural = 'Cовет'


class Chelensoveta(models.Model):

    STATUS_NEWS = (
        ('Publish', 'Опубликовать'),
        ('Not_to_publish', 'Не публиковать'),
    )
    status = models.CharField(default='Publish',max_length=30, choices=STATUS_NEWS, verbose_name='Статус')
    sovet = models.ForeignKey(Sovet, on_delete=models.CASCADE, related_name='chelensoveta')
    title = models.CharField(max_length=255, db_index=True, verbose_name='Имя')
    doljnost = models.CharField(max_length=255, db_index=True, verbose_name='Должность')
    works = models.CharField(max_length=255, db_index=True, verbose_name='Место работы')
    image = models.ImageField(blank=True, upload_to='media/image/', null=True, verbose_name='Фото')
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Члены совета'
        verbose_name_plural = 'Члены совета'



