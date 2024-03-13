from django.db import models
from users.models import User


class FeedbackPost(models.Model):
    description = models.TextField(blank=True,
                                   verbose_name='Отзыв')
    author = models.ForeignKey(User, on_delete=models.PROTECT,
                               blank=False, related_name='authors',
                               verbose_name='автор')

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'