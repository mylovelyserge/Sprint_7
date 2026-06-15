# Sprint 7 — API-тесты сервиса «Яндекс Самокат»

Автотесты на Python (pytest + requests) для API учебного сервиса
[Яндекс Самокат](https://qa-scooter.praktikum-services.ru/docs/).

## Что протестировано

### Основное задание
- **Создание курьера** — `POST /api/v1/courier`
- **Логин курьера** — `POST /api/v1/courier/login`
- **Создание заказа** — `POST /api/v1/orders` (с параметризацией по цвету)
- **Список заказов** — `GET /api/v1/orders`

### Дополнительное задание
- **Удалить курьера** — `DELETE /api/v1/courier/{id}`
- **Принять заказ** — `PUT /api/v1/orders/accept/{id}?courierId={id}`
- **Получить заказ по номеру** — `GET /api/v1/orders/track?t={track}`

## Структура проекта

```
Sprint_7/
├── data.py        # URL, эндпоинты, тексты ошибок, тело заказа
├── helper.py      # вспомогательные функции (генерация данных, запросы)
├── conftest.py    # фикстуры (создание/удаление тестовых данных)
└── tests/
    ├── test_create_courier.py
    ├── test_login_courier.py
    ├── test_create_order.py
    ├── test_orders_list.py
    ├── test_delete_courier.py
    ├── test_accept_order.py
    └── test_get_order_by_track.py
```

Тесты для каждой ручки лежат в отдельном классе. Все тесты независимы,
тестовые данные создаются перед тестом и удаляются после.

## Установка

Проект использует [uv](https://docs.astral.sh/uv/):

```bash
uv sync
```

## Запуск тестов

```bash
uv run pytest
```

## Отчёт Allure

Результаты прогона складываются в `allure-results/`
(настроено в `pyproject.toml`). Для генерации и просмотра отчёта нужен
[Allure CLI](https://allurereport.org/docs/install/):

```bash
# открыть отчёт во временном веб-сервере
allure serve allure-results

# либо сгенерировать статический отчёт в папку allure-report
allure generate allure-results -o allure-report --clean
```

Чтобы закоммитить только отчёт:

```bash
git add -f allure-report
git commit -m "add allure report"
git push
```
