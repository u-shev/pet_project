# Generated by Django 4.2.11 on 2024-03-12 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Кейс')),
                ('picture', models.FileField(upload_to='media/upload/', verbose_name='Выберите картинку')),
            ],
            options={
                'verbose_name': 'Кейс',
                'verbose_name_plural': 'Кейсы',
            },
        ),
    ]
