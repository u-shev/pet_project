# Generated by Django 4.2.11 on 2024-03-14 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('video_link', models.CharField(max_length=150, verbose_name='Ссылка на видео, то, что в кавычках, вместе с кавычками')),
                ('pictures', models.FileField(upload_to='media/upload/', verbose_name='Загрузите картинку')),
            ],
            options={
                'verbose_name': 'Lesson',
                'verbose_name_plural': 'Lessons',
            },
        ),
    ]
