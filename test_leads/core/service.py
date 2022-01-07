import json

import requests
from test_leads.settings import (TG_BOT_TOKEN, TG_CHANEL_ID, VK_ACCESS_TOKEN,
                                 VK_API_VERSION, VK_SECERT_KEY, VK_USER_TOKEN)


def check_secret_key(request) -> bool:
    """ Проверка секретного ключа для уведомлений ВК """
    return json.loads(request.body)['secret'] == VK_SECERT_KEY  # True = Верный


def get_vk_user_info(request) -> dict:
    """ Получить информацию о пользователе ВК """
    data = json.loads(request.body)

    url = [
        'https://api.vk.com/method/users.get',
        f'?user_id={data["object"]["message"]["from_id"]}',
        f'&v={VK_API_VERSION}',
        f'&access_token={VK_USER_TOKEN}'
    ]

    response = requests.post(''.join(url)).json()
    return response["response"][0]


def get_userid_and_messageid(request) -> dict:
    """ Получить ID пользователя ВК и ID сообщения в группу ВК """
    data = json.loads(request.body)
    return {
        'user_id': data["object"]["message"]["from_id"],
        'message_id': data["object"]["message"]["id"]
    }


def send_message_telegram(vk_user) -> None:
    """ Отправить сообщение в телеграм """
    url = [
        f'https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage',
        f'?chat_id={TG_CHANEL_ID}',
        '&parse_mode=Markdown',
        f'&text=Пишет новый пользователь {vk_user["first_name"]} {vk_user["last_name"]}!'
    ]

    response = requests.get(''.join(url)).json()

    if response['ok'] is False:
        # Если запрос завершился неудачей
        raise Exception(
            f'error_code: {response["error_code"]}; description: {response["description"]}'
        )


def send_message_vk(vk_user_id, message) -> None:
    """ Отправить сообщение пользователю ВК от имени сообщества """
    url = [
        'https://api.vk.com/method/messages.send',
        f'?user_id={vk_user_id}',
        f'&v={VK_API_VERSION}',
        f'&access_token={VK_ACCESS_TOKEN}',
        f'&message={message}',
        '&random_id=0'
    ]
    response = requests.get(''.join(url)).json()

    if 'error' in response:
        # Если запрос завершился неудачей
        raise Exception(
            f'error_code: {response["error"]["error_code"]}; description: {response["error"]["error_msg"]}'
        )


class TGWebHook:
    """ Telegram web hook """
    def get():
        """ Получить telegram web hook """
        url = f'https://api.telegram.org/bot{TG_BOT_TOKEN}/getWebhookInfo'
        response = requests.get(url).json()
        return response

    def set():
        """ Установить telegram web hook """
        # URL на который будет отправляться уведомление о
        # новом сообщении в телеграм группе
        urlset = 'https://853a-85-115-248-33.ngrok.io/tg_group_new_message'
        # На какие объекты в группе будет реагировать

        url = [
            f'https://api.telegram.org/bot{TG_BOT_TOKEN}/setWebhook',
            f'?url={urlset}',
            '&allowed_updates=[message,callback_query]'
        ]
        response = requests.get(''.join(url)).json()
        return response

    def delete():
        """ Удалить telegram web hook """
        url = f'https://api.telegram.org/bot{TG_BOT_TOKEN}/deleteWebhook'
        response = requests.get(url).json()
        return response
