# Generated by Django 3.1.12 on 2021-07-27 14:47

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sovet', '0008_sovet_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='sovet',
            name='content_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='sovet',
            name='content_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]
