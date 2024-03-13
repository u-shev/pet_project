from django.db import models
from users.models import User


class Lesson(models.Model):
    name = models.CharField(max_length=150, blank=False,
                            verbose_name='Название')
    description = models.TextField(blank=True,
                                   verbose_name='Description')
    video_link = models.CharField(max_length=150, blank=False,
                            verbose_name='Ссылка на видео, то, что в кавычках, вместе с кавычками')
    pictures = models.FileField(upload_to='media/upload/',
                               verbose_name='Загрузите картинку')

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.picture.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'