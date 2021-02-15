![workflow primorsk-cup](https://github.com/Bazulenkov/primorsk-cup/workflows/primorsk-cup%20CI%2fCD/badge.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

# primorsk-cup

Сайт для регистрации спортсменов на "Кубок Приморска".

## Installing

### Запуск проекта на локальном компьютере (на примере Linux)

Эти инструкции помогут вам создать копию проекта и запустить ее на локальном компьютере для целей разработки и тестирования.
Запуск проекта (на примере Linux)

Перед тем, как начать: У вас должен быть установлен пакет "python3"

- Создайте на своем компютере папку проекта `mkdir Primorsk-cup` и перейдите в нее `cd Primorsk-cup`
- Склонируйте этот репозиторий в текущую папку `git clone https://github.com/Bazulenkov/primorsk-cup`
- Создайте виртуальное окружение `python3 -m venv venv`
- Активируйте виртуальное окружение `source venv/bin/activate`
- Создайте файл `.env` командой `touch .env` и добавьте в него переменные окружения:
```
SECRET_KEY = #секретный ключ Django
DEBUG=1
```
Сгенерировать SECRET_KEY вы можете, например, по этой статье https://tech.serhatteker.com/post/2020-01/django-create-secret-key/
- Установите зависимости `pip install -r requirements.txt`
- Создайте все необходимые таблицы в базе данных - выполните команду `./manage.py migrate`   
- Создайте администратора сайта `./manage.py createsuperuser` (Администратор тоже будет отображаться в списках участников - поэтому после создания администратора, нужно зайти в админку, и добавить все недостающие поля в запись администратора) 

Чтобы запустить проект на локальной машине - `./manage.py runserver`

### Деплой на удаленный сервер

#### Установка Docker
Установите Docker, используя инструкции с официального сайта:
- для [Windows и MacOS](https://www.docker.com/products/docker-desktop) 
- для [Linux](https://docs.docker.com/engine/install/ubuntu/). Отдельно потребуется установть [Docker Compose](https://docs.docker.com/compose/install/)

#### Запуск docker-compose
- Поменяйте в файле `.env` настройки `DEBUG=0`
- Добавьте в файл `.env` переменные окружения для работы с базой данных:
```
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД 
```
- Скопируйте на сервер файлы `docker-compose.yaml`, `.env`, `Dockerfile-nginx`, `nginx.conf` командами:
```
scp docker-compose.yaml  {user}@{server-ip}:
scp .env {user}@{server-ip}:
scp Dockerfile-nginx {user}@{server-ip}:

```
- Запустите docker-compose командой `sudo docker-compose up -d` 
- Накатите миграции `sudo docker-compose exec app python manage.py migrate`
- Соберите статику командой `sudo docker-compose exec app python manage.py collectstatic --no-input`
- Импортируйте теги в базу - выполните команду `sudo docker-compose exec app ./manage.py load_discipline`
- Создайте суперпользователя Django `sudo docker-compose exec app python manage.py createsuperuser --username admin --email 'admin@yamdb.com'`

## CI/CD
### Для автоматического деплоя на сервер необходимо:
- создать переменные окружения в разделе `secrets` настроек текущего репозитория:
```
DOCKER_PASSWORD # Пароль от Docker Hub
DOCKER_USERNAME # Логин от Docker Hub
HOST # Публичный ip адрес сервера
USER # Пользователь зарегистрированный на сервере
PASSPHRASE # Если ssh-ключ защищен фразой-паролем
SSH_KEY # Приватный ssh-ключ
TELEGRAM_TO # ID телеграм-аккаунта
TELEGRAM_TOKEN # Токен бота
```

### После каждого обновления репозитория (`git push`) будет происходить:
1. Проверка кода на стандарты `PEP8`.
2. Сборка и публикация образа на `Docker Hub`.
3. Автоматический деплой.
4. Отправка уведомления в персональный чат Telegram.

## Built With
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Pillow](https://pypi.org/project/Pillow/)
- [Sorl-thumbnail](https://pypi.org/project/sorl-thumbnail/)
- [WeasyPrint](https://weasyprint.org/) 
- [PostgreSQL](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)
- [Gunicorn](https://gunicorn.org/)
- [NGINX](https://nginx.org)
- [GitHub Actions](https://github.com/features/actions)

## Authors

* **Anton Bazulenkov** - *Initial work* - [Bazulenkov](https://github.com/Bazulenkov)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details