# Generated by Django 3.2.22 on 2023-10-14 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_hotel', models.CharField(max_length=150, verbose_name='Название отеля')),
                ('telephone', models.CharField(max_length=150, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=200, verbose_name='Адрес')),
                ('ds', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('du', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
            ],
            options={
                'verbose_name': 'Контакты',
                'verbose_name_plural': 'Контакты',
                'ordering': ['name_hotel'],
            },
        ),
    ]
