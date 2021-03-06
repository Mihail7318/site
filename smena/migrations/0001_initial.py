# Generated by Django 2.2.2 on 2021-07-26 17:51

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название рубрики')),
                ('name_en', models.CharField(max_length=250, null=True, verbose_name='Название рубрики')),
                ('name_ru', models.CharField(max_length=250, null=True, verbose_name='Название рубрики')),
            ],
            options={
                'verbose_name': 'рубрики смены',
                'verbose_name_plural': 'рубрика смены',
            },
        ),
        migrations.CreateModel(
            name='Smena',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Publish', 'Опубликовать'), ('Not_to_publish', 'Не публиковать')], default='P', max_length=30, verbose_name='Статус')),
                ('yved', models.BooleanField(default=False, verbose_name='Уведомить')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Наименование')),
                ('title_en', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Наименование')),
                ('title_ru', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True, verbose_name='Ссылка')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Описание')),
                ('content_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание')),
                ('content_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/image/', verbose_name='Изображение')),
                ('views', models.IntegerField(default=0, verbose_name='Количество просмотров')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('rubric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smena.Rubric', verbose_name='Рубрика')),
            ],
            options={
                'verbose_name': 'Профильная смена',
                'verbose_name_plural': 'Профильные смены',
                'ordering': ['-created_at'],
            },
        ),
    ]
