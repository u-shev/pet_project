# Generated by Django 4.2.11 on 2024-03-14 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name': 'Урок', 'verbose_name_plural': 'Уроки'},
        ),
    ]
