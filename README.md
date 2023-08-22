# UsefulHH

## Description
Данное Rest приложение предоставляет интерфейс для удобного просмотра/парсинга вакансий в сфере IT с платформы HeadHunter, которые содержат только важную информацию.

Существует три узла для взаимодействия:

* Вывод 30 актуальных вакансий
* Вывод вакансий, в названии которых содержится введенное ключевое слово
* Проверка HeadHunter на наличие новых вакансий и их добавление в базу данных

Используемый стек технологий:

* Python 3.11
* FastAPI 0.95.2
* SQLAlchemy 2.0.15
* Pydantic 1.10.8
* Alembic 1.11.1

## Requirements

Python 3.11+

Сервер PostgreSQL

## Installation

Нужно создать виртуальное окружение. Далее с помощью следующих команд уставить нужные для работы библиотеки:


Установка FastAPI с Uvicorn
```console
$ pip install fastapi[all]

---> 100%
```

Также можно установить их отдельно
```console
$ pip install fastapi
$ pip install uvicorn

---> 100%
```

Установка SQLAlchemy
```console
$ pip install sqlalchemy

---> 100%
```

Установка Pydantic
```console
$ pip install pydantic

---> 100%
```

Установка Alembic
```console
$ pip install alembic

---> 100%
```

После установки необходимых пакетов, нужно создать и заполнить файл окружения `.env`. Он должен содержать следующие переменные:

```Python
DB_HOST=localhost
DB_PORT=5432
DB_NAME=restproject
DB_USER=postgres
DB_PASS=password
SERVER_HOST=127.0.0.1
SERVER_PORT=8000
```

Если у вас другие значения - замените их.

### Run it

Вначале проверьте, запущен ли сервер PostgreSQL.

Запустите приложение через консоль с помощью:

```console
$ uvicorn main:app --reload

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28720]
INFO:     Started server process [28722]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

Или запустите вручную файл `main.py` с помощью вашей IDE.

### Check it

Проверить работу можно перейдя по ссылке <a href="http://127.0.0.1:8000/" class="external-link" target="_blank">http://127.0.0.1:8000/</a>.

Вы увидите:

```JSON
{
  "vacancies": {
    "additionalProp1": {
      "company_name": "string",
      "city": "string",
      "vacancy_name": "string",
      "salary_from": 0,
      "salary_to": 0,
      "salary_currency": "string",
      "work_experience": "string",
      "employment": "string",
      "published_at": "2023-08-22T14:56:08.136Z",
      "vacancy_url": "string",
      "requirement": "string",
      "responsibility": "string"
    },
    "additionalProp2": {
      "company_name": "string",
      "city": "string",
      "vacancy_name": "string",
      "salary_from": 0,
      "salary_to": 0,
      "salary_currency": "string",
      "work_experience": "string",
      "employment": "string",
      "published_at": "2023-08-22T14:56:08.136Z",
      "vacancy_url": "string",
      "requirement": "string",
      "responsibility": "string"
    },
    "additionalProp3": {
      "company_name": "string",
      "city": "string",
      "vacancy_name": "string",
      "salary_from": 0,
      "salary_to": 0,
      "salary_currency": "string",
      "work_experience": "string",
      "employment": "string",
      "published_at": "2023-08-22T14:56:08.136Z",
      "vacancy_url": "string",
      "requirement": "string",
      "responsibility": "string"
    }
  }
}
```

Узлы API:

* Базовый путь `/`.
* Путь `/search_vacancies?search_text={search_text}` с параметром `search_text`, который должен быть типа `str`.
* Путь `/parse_new_vacancies`.

Проверить работу также можно используя интерактивную документацию <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a>.
