# Generated by Django 3.1.12 on 2021-07-27 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cust', '0007_auto_20210726_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='image',
            field=models.ImageField(default=1, upload_to='', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]