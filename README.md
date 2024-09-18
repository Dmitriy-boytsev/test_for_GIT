# Django TODO Project
## Описание
Это веб-приложение на Django для управления задачами (TODO). Приложение поддерживает аутентификацию пользователей и работу с задачами, используя Django и базу данных PostgreSQL. Проект использует контейнеризацию с помощью Docker для упрощения развертывания. Создано API для следующих действий:

- **Создание задачи**: Пользователь может создать новую задачу.
- **Просмотр списка задач**: Пользователь может получить список всех задач.
- **Просмотр задачи по ID**: Пользователь может получить задачу по её уникальному ID.
- **Редактирование задачи**: Пользователь может редактировать существующую задачу.
- **Удаление задачи**: Пользователь может удалять задачу.

### Примеры API-запросов
- **Создать задачу (POST)**: `/api/tasks/`
- **Просмотреть все задачи (GET)**: `/api/tasks/`
- **Просмотреть задачу по ID (GET)**: `/api/tasks/{id}/`
- **Редактировать задачу (PUT)**: `/api/tasks/{id}/`
- **Удалить задачу (DELETE)**: `/api/tasks/{id}/`
- **Принять запрос от клиента о пользователе** `/api/users/{users_id}`

## Автотесты для CRUD операций
Для проверки функциональности API разработаны автотесты, покрывающие следующие действия:

## Автотесты для users на pytest

- **Создание задачи**.
- **Просмотр списка задач**.
- **Просмотр отдельной задачи по ID**.
- **Редактирование задачи**.
- **Удаление задачи**.

## Основные технологии
- **Django**: Web-фреймворк для Python, используемый для создания приложения.
- **PostgreSQL**: СУБД для хранения данных.
- **Docker**: Используется для контейнеризации приложения и базы данных.
- **Django REST Framework**: Для реализации API (если используется API).
- **FastAPI**: Для Интеграции с внешним API (DRF)

## Требования
- Docker
- Docker Compose

## Запуск проекта

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/ваш-репозиторий.git
   cd ваш-репозиторий

2. Создайте файл .env в корне проекта, если его нет. Пример содержания .env файла:

   ```bash
    SECRET_KEY='ваш-секретный-ключ'
    DB_HOST=db
    DB_PORT=5432
    DB_USER=postgres
    DB_PASSWORD=postgres
    DB_NAME=postgres

3. Соберите и запустите контейнеры с помощью Docker Compose:
    docker-compose up --build
