import json

from django.db import IntegrityError
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from . import service
from .models import Message


# На localhost без csrf_exempt ошибка: "403 Forbidden (CSRF cookie not set.)"
@csrf_exempt
def vk_group_new_message(request) -> HttpResponse:
    """ Событие, когда ВК присылает уведомление
    о том, что пришло новое сообщение """
    if not service.check_secret_key(request):
        raise Exception('VK secret key is invalid')

    # Получаем необходимые данные
    vk_user = service.get_vk_user_info(request)
    info = service.get_userid_and_messageid(request)

    try:
        # Записываем в БД
        Message.objects.create(
            message_id=info['message_id'],
            vk_user_id=info['user_id'],
            first_name=vk_user["first_name"],
            last_name=vk_user["last_name"]
        )

        # Отправляем сообщение в телеграм
        service.send_message_telegram(vk_user)
    except IntegrityError as e:
        # ВК отправляет два одинаковых уведомления на одно
        # новое сообщение в группе ВК, поэтому здесь будет
        # исключение при попытке записать одинаковые уведомления,
        # тем самым, исключая дубликаты в базе
        pass

    return HttpResponse(status=200)


@csrf_exempt
def vk_check(request) -> HttpResponse:
    """ Проверка ВК для подтверждения URL адреса """
    # Возвращаем код, который требует ВК
    return HttpResponse('vkcode123')


@csrf_exempt
def tg_group_new_message(request) -> HttpResponse:
    """ Событие, когда webhook телеграм бота присылает
    уведомление о том, что в группе новое сообщение.
    Все новые сообщения будут отправляться последнему
    написавшему в группу ВК пользователю """
    data = json.loads(request.body)

    if data['message']['from']['is_bot'] is False:
        # Если отправитель не является ботом
        try:
            message = data['message']['text']
            # Получаем ID пользователя ВК который написал последним
            vk_user_id = Message.objects.latest().vk_user_id
            service.send_message_vk(vk_user_id, message)
        except Message.DoesNotExist:
            # Здесь, скорее всего пустая база
            pass
        except KeyError as e:
            # Если не найден "text", то в чат был отправлен
            # стикер или что-то другое
            if not "'text'" == str(e):
                raise

    return HttpResponse(status=200)
