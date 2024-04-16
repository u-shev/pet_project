from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=150, blank=False,
                            verbose_name='Название')
    description = models.TextField(blank=True,
                                   verbose_name='Кейс')
    picture = models.FileField(upload_to='media/upload/',
                               verbose_name='Выберите картинку')

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.picture.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Кейс'
        verbose_name_plural = 'Кейсы'


class Picture(models.Model):
    name = models.CharField(max_length=150, blank=False,
                            verbose_name='Название')
    picture = models.FileField(upload_to='media/upload/main/',
                               verbose_name='Выберите картинку')

    class Meta:
        verbose_name = 'Картинка для оформления'
        verbose_name_plural = 'Картинки для оформления'
