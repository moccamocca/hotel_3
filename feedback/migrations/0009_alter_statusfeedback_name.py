# Generated by Django 3.2.22 on 2023-10-29 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0008_alter_statusfeedback_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statusfeedback',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Статус'),
        ),
    ]
