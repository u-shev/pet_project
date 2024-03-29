# Generated by Django 4.2.11 on 2024-03-14 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_alter_lesson_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='pictures',
            field=models.FileField(upload_to='media/upload/lessons/', verbose_name='Загрузите картинку'),
        ),
        migrations.CreateModel(
            name='LessonAdditionalVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_link', models.CharField(max_length=250, verbose_name='Ссылка на дополнительное видео')),
                ('related_lesson', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lesson_video', to='lessons.lesson', verbose_name='урок')),
            ],
            options={
                'verbose_name': 'Доп.видео для уроков',
                'verbose_name_plural': 'Доп.видео для уроков',
            },
        ),
        migrations.CreateModel(
            name='LessonAdditionalPicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pictures', models.FileField(upload_to='media/upload/lessons/', verbose_name='Загрузите дополнительную картинку')),
                ('related_lesson', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lesson_picure', to='lessons.lesson', verbose_name='урок')),
            ],
            options={
                'verbose_name': 'Доп.картинка для уроков',
                'verbose_name_plural': 'Доп.картинки для уроков',
            },
        ),
    ]
