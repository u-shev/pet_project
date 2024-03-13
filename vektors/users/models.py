from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'