# Generated by Django 2.2.2 on 2021-07-26 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='complain',
            name='text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
