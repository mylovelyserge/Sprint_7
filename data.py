class Urls:
    """Базовый URL и эндпоинты API сервиса Яндекс Самокат."""

    BASE_URL = 'https://qa-scooter.praktikum-services.ru'

    CREATE_COURIER = '/api/v1/courier'
    LOGIN_COURIER = '/api/v1/courier/login'
    DELETE_COURIER = '/api/v1/courier/{id}'

    CREATE_ORDER = '/api/v1/orders'
    GET_ORDERS = '/api/v1/orders'
    ACCEPT_ORDER = '/api/v1/orders/accept/{id}'
    GET_ORDER_BY_TRACK = '/api/v1/orders/track'


class CourierMessages:
    """Сообщения об ошибках ручек, связанных с курьером."""

    NOT_ENOUGH_DATA_TO_CREATE = 'Недостаточно данных для создания учетной записи'
    LOGIN_ALREADY_USED = 'Этот логин уже используется. Попробуйте другой.'
    NOT_ENOUGH_DATA_TO_LOGIN = 'Недостаточно данных для входа'
    ACCOUNT_NOT_FOUND = 'Учетная запись не найдена'
    COURIER_NOT_FOUND = 'Курьера с таким id нет.'


class OrderMessages:
    """Сообщения об ошибках ручек, связанных с заказом."""

    NOT_ENOUGH_DATA_TO_SEARCH = 'Недостаточно данных для поиска'
    COURIER_NOT_EXISTS = 'Курьера с таким id не существует'
    ORDER_NOT_EXISTS = 'Заказа с таким id не существует'
    ORDER_NOT_FOUND = 'Заказ не найден'


# Базовые данные для создания заказа.
# Цвет (color) задаётся отдельно в параметризованных тестах.
ORDER_PAYLOAD = {
    'firstName': 'Naruto',
    'lastName': 'Uchiha',
    'address': 'Konoha, 142 apt.',
    'metroStation': 4,
    'phone': '+7 800 355 35 35',
    'rentTime': 5,
    'deliveryDate': '2020-06-06',
    'comment': 'Saske, come back to Konoha',
}
