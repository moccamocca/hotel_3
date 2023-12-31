# Generated by Django 3.2.22 on 2023-10-28 15:25

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_alter_booking_number_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='number_booking',
            field=models.CharField(max_length=50, unique=True, verbose_name='Номер бронирования'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='patronymic',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='booking',
            name='surname',
            field=models.CharField(max_length=100, verbose_name='Фамилия'),
        ),
    ]
