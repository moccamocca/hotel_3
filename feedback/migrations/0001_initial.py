# Generated by Django 3.2.22 on 2023-10-14 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIO', models.CharField(max_length=100, verbose_name='ФИО')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('ds', models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')),
                ('date_close', models.DateTimeField(blank=True, default='', verbose_name='Дата закрытия')),
            ],
        ),
    ]