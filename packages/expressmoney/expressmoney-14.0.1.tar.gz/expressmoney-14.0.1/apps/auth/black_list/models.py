from django.db import models
from django.conf import settings


class BlackList(models.Model):
    created = models.DateTimeField('Добавлен', auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    comment = models.CharField('Комментарий', max_length=128, blank=True)

    def __str__(self):
        return f'{self.user_id}'

    class Meta:
        verbose_name = 'Черный список'
        verbose_name_plural = 'Черный список'
