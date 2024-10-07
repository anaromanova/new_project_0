# Проект Python

## Описание:

Проект Python - это виджет банковских операций клиента на Python.

Реализовыван новый модуль для банковского приложения,
который включает в себя фильтрацию транзакций по определенной валюте 
и получение описания каждой операции.

UPDATE: Разработан декоратор log, который будет автоматически регистрировать 
детали выполнения функций, такие как время вызова, имя функции,
передаваемые аргументы, результат выполнения и информация об ошибках.
Это позволит обеспечить более глубокий контроль и анализ поведения
программы в процессе ее выполнения.

## Установка:

Клонируйте репозиторий:
```
git clone https://github.com/anaromanova/new_project_0.git
```

## Документация:

Для получения дополнительной информации обратитесь к [документации](docs/README.md).

## Тестирование:

Наш проект покрыт тестами pytest. Для их запуска выполните команду:
```
pytest
```