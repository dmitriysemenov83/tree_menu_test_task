# 🧩 Django Tree Menu — Тестовое задание
Это приложение реализует древовидное меню с произвольной вложенностью, управляемое через стандартную админку Django.

## 📦 Требования

Python 3.11+

Django 5.2+

SQLite (по умолчанию)

---

## 🚀 Запуск проекта
```bash
git clone https://github.com/dmitriysemenov83/tree_menu_test_task
cd tree_menu_test_task
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata menu/fixtures/initial_data.json
python manage.py runserver
```

## 🛠 Возможности
- Меню хранится в базе данных (SQLite).

- Добавление/редактирование меню через Django Admin.

- Активный пункт определяется по текущему URL.

- Все родительские уровни над активным раскрыты.

- Отрисовка меню выполняется через template tag:
```
{% load menu_tags %}
{% draw_menu 'main_menu' %}
```
- Поддержка нескольких меню (по имени).

- URL может быть указан как вручную (/products/laptops/), так и через named_url.

## 📁 Структура фикстур
Фикстуры сохранены в:

```
menu/fixtures/initial_data.json
```
Загружаются командой:

```
python manage.py loaddata menu/fixtures/initial_data.json
```

## 🧪 Примеры URL
- / — Главная

- /about/ — О нас

- /products/ — Продукты

- /products/laptops/ — Ноутбуки (вложенность работает)
