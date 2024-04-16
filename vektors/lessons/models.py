from django.db import models


class Lesson(models.Model):
    permission_required = 'lesson.view_lesson'
    name = models.CharField(max_length=150, blank=False,
                            verbose_name='Название')
    description = models.TextField(blank=True,
                                   verbose_name='Description')
    video_link = models.CharField(max_length=150, blank=False,
                                  verbose_name='Ссылка на видео, \
                                    вместе с кавычками')
    pictures = models.FileField(upload_to='media/upload/lessons/',
                                verbose_name='Загрузите картинку')

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.picture.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class LessonAdditionalPicture(models.Model):
    pictures = models.FileField(upload_to='media/upload/lessons/',
                                verbose_name='Загрузите доп. картинку')
    p_related_lesson = models.ForeignKey(Lesson, on_delete=models.PROTECT,
                                         default=1, blank=False,
                                         related_name='p_related_lessons',
                                         verbose_name='урок')

    class Meta:
        verbose_name = 'Доп.картинка для уроков'
        verbose_name_plural = 'Доп.картинки для уроков'


class LessonAdditionalVideo(models.Model):
    name = models.CharField(max_length=150, blank=False,
                            verbose_name='Название видео')
    video_link = models.CharField(max_length=250, blank=False,
                                  verbose_name='Ссылка на \
                                    дополнительное видео')
    v_related_lesson = models.ForeignKey(Lesson, on_delete=models.PROTECT,
                                         default=1, blank=False,
                                         related_name='v_related_lessons',
                                         verbose_name='урок')

    class Meta:
        verbose_name = 'Доп.видео для уроков'
        verbose_name_plural = 'Доп.видео для уроков'
