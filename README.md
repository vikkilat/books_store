# REST API для интернет-магазина по продаже книг

Проект позволяет получить все книги, книги определенной категории и её подкатегорий, конкретной книги. В проекте настроена авторизация, форма обратной связи и админ панель.


## Стек технологий:

* Python 3.10
* Django 4.2
* Django Rest Framework
* PostgreSQL
* Docker
* DRF-YASG для документации

## Как запустить проект:

* Клонировать репозиторий:

```
git clone https://github.com/vikkilat/books_store.git
```

* Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

* Установить зависимости из файла ```requirements.txt```:

```
pip install -r requirements.txt
```

* Запустить проект:
```
docker-compose up -d --build
```

## Автор:
[Латышева Виктория](https://github.com/vikkilat)