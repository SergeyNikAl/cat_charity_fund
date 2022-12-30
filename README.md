## Благотворительный фонд поддержки котиков (QRKot)

### 1. [Описание](#1)
### 2. [База данных и переменные окружения](#2)
### 3. [Команды для запуска](#3)
### 4. [Работа с API](#4)
### 5. [Стек технологий](#5)
### 6. [Об авторе](#6)

---
### 1. Описание <a id=1></a>

Проект сервиса для поддержки котиков (QRKot) предоставляет пользователям следующие возможности:  
#### Неавторизованные пользователи:
  - могут зарегистрироваться
  - просматривать все проекты фонда
#### Зарегистрированные (авторизованные) пользователи:
  - могут делать то же, что и неавторизованные пользователи
  - осуществлять пожертвования на любую сумму и оставлять комментарии к ним
  - просматривать свои пожертвования
  - просматривать и редактировать свой аккаунт
#### Суперпользователи:
  - могут делать то же, что и обычные пользователи
  - созавать благотворительные проекты, редактировать их и удалять
  - просматривать все пожертвования сделанные в фонд
  - просматривать и редактировать аккаунты всех пользователей

---
### 2. База данных и переменные окружения <a id=2></a>

Проект использует базу данных SQLite.  
Для подключения и выполнения запросов к базе данных необходимо создать и заполнить файл ".env" с переменными окружения в корневой папке проекта.  
Пример:
```bash
APP_TITLE=Благотворительный фонд поддержки котиков QRKot
DESCRIPTION=Сервис для поддержки котиков
DATABASE_URL=sqlite+aiosqlite:///./qrkot.db
SECRET=#Придумайте секретный код
FIRST_SUPERUSER_EMAIL=superuser@superuser.ru
FIRST_SUPERUSER_PASSWORD=qwer1234
MIN_PASSWORD_LENGTH=3
```

---
### 3. Команды для запуска <a id=3></a>

Перед запуском необходимо склонировать проект:
```bash
HTTPS: git clone https://github.com/SergeyNikAl/cat_charity_fund
```

Cоздать и активировать виртуальное окружение:
```bash
python -m venv venv
```
```bash
Linux: source venv/bin/activate
Windows: source venv/Scripts/activate
```

И установить зависимости из файла requirements.txt:
```bash
python3 -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

Выполнить миграции:
```bash
alembic upgrade head
```

Запустить проект можно командой:
```bash
uvicorn app.main:app --reload
```

Теперь доступность проекта можно проверить по адресу [http://localhost:8000/](http://localhost:8000/)  
Посмотреть документацию по API проекта можно по адресам:<a id=API></a>
  - Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)
  - ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---
### 4. Работа с API <a id=4></a>

#### Доступные эндпоинты:
```
"/charity_project/"
"/charity_project/{project_id}/"
"/donation/"
"/donation/my"
"/auth/jwt/login"
"/auth/jwt/logout"
"/auth/register"
"/users/me"
"/users/{id}"
```

#### Примеры запросов:
- Получение всех проектов фонда:
```
Method: GET
Endpoint: "/charity_project/"
```

- Создание благотворительного проекта:
```
Method: POST
Endpoint: "/charity_project/"
Payload:
{
    "name": "string",
    "description": "string",
    "full_amount": 0
}
```

- Осуществление пожертвования:
```
Method: POST
Endpoint: "/donation/"
Payload:
{
  "full_amount": 0,
  "comment": "string"
}
```

- Получить список всех своих пожертвований:
```
Method: GET
Endpoint: "/donation/my"
```

---
### 5. Стек технологий <a id=5></a>

- [Python](https://www.python.org/)
- [Flask](https://flask.org/)
- [FasAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/)
- [Pydantic](https://docs.pydantic.dev/)
- [Uvicorn](https://www.uvicorn.org/)

---
### 6. Об авторе <a id=6></a>

- [Сергей Никулин](https://github.com/SergeyNikAl)