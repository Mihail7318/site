# Generated by Django 3.1.12 on 2021-07-26 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sovet', '0005_auto_20210725_1323'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chelensoveta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Publish', 'Опубликовать'), ('Not_to_publish', 'Не публиковать')], default='Publish', max_length=30, verbose_name='Статус')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Имя')),
                ('title_en', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Имя')),
                ('title_ru', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Имя')),
                ('doljnost', models.CharField(db_index=True, max_length=255, verbose_name='Должность')),
                ('doljnost_en', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Должность')),
                ('doljnost_ru', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Должность')),
                ('works', models.CharField(db_index=True, max_length=255, verbose_name='Место работы')),
                ('works_en', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Место работы')),
                ('works_ru', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Место работы')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/image/', verbose_name='Фото')),
                ('views', models.IntegerField(default=0, verbose_name='Количество просмотров')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
            ],
            options={
                'verbose_name': 'Попечительский совет',
                'verbose_name_plural': 'Попечительский совет',
            },
        ),
        migrations.CreateModel(
            name='Sovet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Название')),
                ('title_en', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Название')),
                ('title_ru', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Cовет',
                'verbose_name_plural': 'Cовет',
            },
        ),
        migrations.DeleteModel(
            name='Exsov',
        ),
        migrations.DeleteModel(
            name='Popsov',
        ),
        migrations.AddField(
            model_name='chelensoveta',
            name='sovet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chelensoveta', to='sovet.sovet'),
        ),
    ]