from django.db import models


class Message(models.Model):
    """ Сообщения от пользователей ВК """
    message_id = models.CharField('ID сообщения', max_length=255, unique=True)
    vk_user_id = models.CharField('ID пользователя ВК', max_length=255)
    first_name = models.CharField('Имя', max_length=255)
    last_name = models.CharField('Фамилия', max_length=255)
    timestamp = models.DateTimeField(
        'Создано', auto_now=False, auto_now_add=True
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        get_latest_by = "message_id"
