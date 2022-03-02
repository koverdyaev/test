# Test Project

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Демонстрационный проект.
Задачи создаются с помощью API на django и "обрабатываются" при помощи воркера celery.


## Запуск и проверка
Проект проще всего запустить через docker-compose `docker-compose -f local.yml up`.
* Список и создание задач - http://localhost:8000/tasks/
* Документация API - http://localhost:8000/api/docs/
* Проверка статуса задач celery через Flower - http://localhost:5555/tasks, логин и пароль для Flower лежат в .envs/.local/.django 


