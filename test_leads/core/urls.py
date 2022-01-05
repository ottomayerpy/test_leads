from django.urls import path
from . import views

urlpatterns = [
    # После проверки от ВК, заменить vk_check на vk_group_new_message
    path('vk_group_new_message', views.vk_check, name='vk_group_new_message_url'),
    path('tg_group_new_message', views.tg_group_new_message, name='tg_group_new_message_url')
]
