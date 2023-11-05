
# API_Yatube

REST API для социальной сети блогеров , созданной в рамках учебного курса Яндекс.Практикум

Аутентификация по JWT-токену

Работает со всеми модулями социальной сети Yatube: постами, комментариями, группами, подписчиками

Поддерживает методы GET, POST, PUT, PATCH, DELETE

Предоставляет данные в формате JSON

## Стек технологий
- проект написан на Python с использованием Django REST Framework
- библиотека Simple JWT - работа с JWT-токеном
- система управления версиями - git

## Как запустить проект:

- Клонируйте репозитроий с проектом:
```
git clone git@github.com:Fedor-new-Hope/api_yatube.gite
```
- Установить виртуальное окружение для проекта:
```
python -m venv venv

. venv/bin/activate

pip install -r requirements.txt
```
- Создайте в директории файл .env и поместите туда SECRET_KEY, необходимый для запуска проекта.

- Выполните миграции:
```
python manage.py migrate
```
- Создайте суперпользователя:
```
python manage.py createsuperuser
```
- Запустите сервер:
```
python manage.py runserver
```
____________________________________

Ваш проект запустился на http://127.0.0.1:8000/

Документация доступна по адресу http://localhost:8000/redoc/

С помощью команды *pytest* вы можете запустить тесты и проверить работу модулей

## Аутентификация

Выполните POST-запрос *localhost:8000/api/v1/token/* передав поля username и password.

API вернет JWT-токен в формате:

    {
        "refresh": "ХХХХХХХХХХХ",
        "access": "ХХХХХХХХХХХХ"
    }
    
Токен вернётся в поле access, а данные из поля refresh нужны для обновления токена

При отправке запроcов передавайте токен в заголовке Authorization: Bearer <токен>

## Как работает API_Yatube

##### Пример http-запроса (POST) для создания поста:
```
url = 'http://127.0.0.1/api/v1/posts/'
data = {'text': 'Your post'}
headers = {'Authorization': 'Bearer your_token'}
request = requests.post(url, data=data, headers=headers)
```
##### Ответ API_Yatube:
```
Статус- код 200

{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2020-08-20T14:15:22Z"
}
```
_____________________________________________
##### Пример http-запроса (GET) для получения списка подписчиков:
```
url = 'http://127.0.0.1:8000/api/v1/follow/'
headers = {'Authorization': 'Bearer your_token'}
request = requests.get(api, headers=headers)
```
##### Ответ API_Yatube:
```
Статус- код 200

[
  {
    "user": "string",
    "following": "string"
  }
]
```