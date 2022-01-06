# test_leads
Тестовое задание (Никита Колтман)

## Установка
Далее будет представлена инструкция по установке на локальной машине.

#### Клонируйте данный репозиторий и перейдите в каталог "test_leads".
```
git clone https://github.com/ottomayerpy/test_leads
cd test_leads
```
#### Создайте и активируйте виртуальное окружение python.
```
python3 -m venv env
source env/bin/activate
```
#### Установите зависимости.
```
pip install -r requirements.txt
```
#### Запустить ngrok. После того как получим токен на официальном сайте, запускаем:
```
./ngrok authtoken token123
./ngrok http 8000
```
![ngrok](https://s853sas.storage.yandex.net/rdisk/38bbebec896e7cead1516d466d67224f76c8fe49de18ee6e4dcbc96f130fb25d/61d66802/9YbsZ66YClgagiOyK7XANoVw-bOpsACRdyHwxkMgMETGXSdj3muTSsoQSArdiqBcOdeAGtK9dUT_UVzrBRGRpQ==?uid=1520528922&filename=ngrok2.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=1520528922&fsize=45039&hid=572fa31f8d7a8366d7be9e03863f2380&media_type=image&tknv=v2&etag=b9fb1ccfaf45e6230a1208a2f8f098f3&rtoken=rYZz4JXD9t6p&force_default=yes&ycrid=na-9bfd5ebb1223fd0413a8bc1c53c92b75-downloader4f&ts=5d4e1d4888480&s=f156cfd5ad3129a4ac55207b4a54b9d565e4486c7f26ec21c5644cabc566d2ea&pb=U2FsdGVkX1_V5etD4TnUQiFYv2RvAwdXpJYIOlzbderkd3K8klDkAXDlO-IZcKffCu_37LA-4mw8KJ8bSRIml2GuobV3j_7kT2Wnmtrjueg)

Далее сохраняем URL из поля Forwarding, его нужно будет внести в настройки приложения в ВК, о котором будет далее.  
Данную сессию ngrok закрывать нельзя.

#### Cоздайте файл для настроек ".env".
```
cp .env
```
#### Заполните в нем следующие параметры:
```
SECRET_KEY = secret123
VK_API_VERSION = 5.131
VK_USER_TOKEN = token123
VK_SECERT_KEY = secret123
VK_ACCESS_TOKEN = token123
TG_BOT_TOKEN = token123
TG_CHANEL_ID = -100123456789

db_NAME = ltestdb
db_USER = luser
db_PASSWORD = lpass123
db_HOST = localhost
db_PORT = ''
```
#### Проведите миграции.
```
python3 manage.py migrate
```
#### Активируйте сервер.
```
python3 manage.py runserver
```

## Вконтакте
### 1. Создать приложение
По адресу https://dev.vk.com/ создаем Standalone-приложение и сохраняем ID приложения, оно пригодится позже.

### 2. Ключи доступа
Создайте ключ доступа для сообщений сообщества, он пригодится позже.
![vk1](https://s656sas.storage.yandex.net/rdisk/cbe2a94079f354c7920514303bf98d9e769bf0e624a8ddec77304ec4d02d578b/61d66e06/9YbsZ66YClgagiOyK7XANqgvBpFLoeb6MWglNEGOQOnrR63FiyKmDSAUYwpgXOSdh2fuGafGY7gLHUQHjpO3mQ==?uid=1520528922&filename=11.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=1520528922&fsize=68002&hid=49314883c700a7f466e6e34b3ebf5a8e&media_type=image&tknv=v2&etag=7637db983ede3ec2aac2ed27b0eb0d32&rtoken=zbFRXpTa6FKg&force_default=yes&ycrid=na-6f1d02e709592393098c707142e2b6b1-downloader16h&ts=5d4e230530d80&s=8e441e1386dc3cb72bc8fc8dd6423d8f3cebec6e56943d2ce2c377037fbd4bd3&pb=U2FsdGVkX18cIVtsuEuiaqFXUlMpYxoTFQ3mQFnesZZCxTxw8iJH2b8e8vQ25pQDF395Ekv6NydDwzcV62owaGvkk5d8a1Ow14PPJxgZXDs)

### 3. Callback API
#### 3.1 Настройка URL для уведомлений
В поле адрес вставте URL который получили при запуске ngrok плюс /vk_group_new_message. Выглядеть должен URL примерно так: https://cbfa-85-115-248-64.ngrok.io/vk_group_new_message  
Далее нужно в метод vk_check по пути test_leads/core/views.py вставить строку, которую должен вернуть сервер, и нажать подтвердить.  
Если успешно, то в файле test_leads/core/urls.py заменить метод vk_check на vk_group_new_message.

#### 3.2 Секретный ключ
Ниже сгенерируйте любую комбинацию для секретного ключа и сохраните.  

![vk2](https://s738sas.storage.yandex.net/rdisk/a34712af7d73e8e57c4452f0acda0a18054a1efc2e00bb791c056b8d34231ab3/61d67455/9YbsZ66YClgagiOyK7XANnaX9-Zj8ho4WxLGDTudT9EEAWMUjmGsYTOnQq8R-LFM_mmH8O7B6UbqWkwEcyr8PA==?uid=1520528922&filename=22.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=1520528922&fsize=106183&hid=89924b039b39f31f31cd3c8e8b33eee9&media_type=image&tknv=v2&etag=17f8b059dfdee606e08405b63d0fbf0e&rtoken=bMi42Og11Lpm&force_default=yes&ycrid=na-3cfd7a616fe3fcf3271fe1b394e41aef-downloader3h&ts=5d4e29095ff40&s=70da5895ebf7e330323aba907ad83b40de0ae3ff6ec7abddeea14d967409a417&pb=U2FsdGVkX1_aLZs9idPxORVxO0uo9XRND4Dj3p7i61p0dIPuDqVaZqaAkm9uuthDkV4jbvIdkpqFb3E2i8qn9ukSEjd_jjBUGE8fVnLBC5Y)

#### 3.3 Типы событий
Указываем тип события "Входящее сообщение"
![vk3](https://s756sas.storage.yandex.net/rdisk/95eb89f5c80a889fd6f5ed18a40cb443f67926b4fb23d8e5c28a0b8eb5231b81/61d6739e/9YbsZ66YClgagiOyK7XANs643iQHpDwVhHPPwO6rlojb92LLSZd1CQrNRwlKcP1RMmsE-Dt1eYuI6SW9quS_PQ==?uid=1520528922&filename=33.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=1520528922&fsize=88409&hid=2de52d05f8bd7216d951f7dc42cd6530&media_type=image&tknv=v2&etag=533840bae5a6bd2273b4817377ebb985&rtoken=VOqcYXdpeAiu&force_default=yes&ycrid=na-8dd961008083c5c87ee221e8b0e817af-downloader3h&ts=5d4e285ada380&s=c026cdc19320a93620660d288b0f10afcbe97a91e8e88679b1e416789da56792&pb=U2FsdGVkX18et_wWMkktNLhfS7V7H3eVEES0CMaVzqJLIGUlsYgq7OvH5kjtnUB7lyWLpit-k_aksgSylO-5uVf_9qDLz37W8vKd14ZnwR8)

## Телеграм
### 1. Бот
Создаем бота и сохраняем его токен, он пригодится потом.  
### 2. Группа
Создаем группу, добавляем в нее бота и выдаем ему полномочия админа.  
Сохраняем ID канала. Его можно узнать из "Z" версии web телеграма в адресной строке если перейти в диалог группы.  
Пример: https://web.telegram.org/z/#-1782797997  
Далее нужно добавить цифру 100 после знака минус, в итоге ID группы будет такой: -1001782797997

## Конфиг .env
#### SECRET_KEY
Либо генерируем, либо используем мой: django-insecure-n!z7wu&7#%4t@7uka12t4(4b*k_jxw-)pjy=yv0yy7=4w5673+
#### VK_API_VERSION
Версия вашего VK API. Мой: 5.131
#### VK_USER_TOKEN
Чтобы его получить нужно перейти по адресу: https://oauth.vk.com/authorize?client_id=123456789&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends&response_type=token&v=5.131  
Где client_id это ID вашего Standalone-приложения
#### VK_SECERT_KEY
Это ключ из пункта 3.2 раздела "Вконтакте" выше.
#### VK_ACCESS_TOKEN
Это токен из пункта 2 раздела "Вконтакте" выше.
#### TG_BOT_TOKEN и TG_CHANEL_ID
Эти параметры из пункта 1 и 2 раздела "Телеграм" выше.




