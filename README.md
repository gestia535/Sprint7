# Sprint7
# Тестирование API для сервиса Яндекс.Самокат

Этот проект содержит автотесты для API сервиса Яндекс.Самокат, включая следующие функции:
- Создание курьера
- Логин курьера
- Создание заказа
- Получение списка заказов

Структура репозитория 
В корневой директории проекта вы найдете следующие файлы и папки:

tests.py: включает файлы с тестами для функций. 
test_data: файл с тестовыми данными
helpers.py: файл со вспомогательными функциями
allure_results: JSON-файлы с результатами выполнения тестов для генерации отчетов. 
requirements.txt: список всех внешних зависимостей, необходимых для выполнения тестов. 
README.md: руководство по проекту.

Запуск всех тестов

Для установки зависимостей выполните: pip install -r requirements.txt 
Чтобы запустить все тесты, используйте команду: pytest -v

Генерация отчета о тестировании: allure serve allure_results