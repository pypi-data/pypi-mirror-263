from django.db import models


class BlackList(models.Model):
    created = models.DateTimeField('Добавлен', auto_now_add=True)
    user_id = models.PositiveIntegerField(primary_key=True)
    comment = models.CharField('Комментарий', max_length=128, blank=True)

    def __str__(self):
        return f'{self.user_id}'

    class Meta:
        managed = False
        verbose_name = 'Черный список'
        verbose_name_plural = 'Черный список'
