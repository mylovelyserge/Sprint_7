import random
import string

import requests

from data import Urls, ORDER_PAYLOAD


def generate_random_string(length):
    """Генерирует строку из строчных латинских букв заданной длины."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def generate_courier_data():
    """Возвращает словарь с уникальными данными для регистрации курьера."""
    return {
        'login': generate_random_string(10),
        'password': generate_random_string(10),
        'firstName': generate_random_string(10),
    }


def register_new_courier_and_return_login_password():
    """Регистрирует нового курьера.

    Возвращает список [login, password, firstName], если регистрация
    прошла успешно (код 201), иначе — пустой список.
    """
    login_pass = []

    payload = generate_courier_data()

    response = requests.post(Urls.BASE_URL + Urls.CREATE_COURIER, data=payload)

    if response.status_code == 201:
        login_pass.append(payload['login'])
        login_pass.append(payload['password'])
        login_pass.append(payload['firstName'])

    return login_pass


def login_courier(login, password):
    """Авторизует курьера и возвращает объект ответа."""
    return requests.post(
        Urls.BASE_URL + Urls.LOGIN_COURIER,
        data={'login': login, 'password': password},
    )


def get_courier_id(login, password):
    """Возвращает id курьера по логину и паролю (или None)."""
    response = login_courier(login, password)
    if response.status_code == 200:
        return response.json().get('id')
    return None


def delete_courier(courier_id):
    """Удаляет курьера по id и возвращает объект ответа."""
    return requests.delete(
        Urls.BASE_URL + Urls.DELETE_COURIER.format(id=courier_id)
    )


def create_order(color=None):
    """Создаёт заказ. color — список цветов (например, ['BLACK']) или None."""
    payload = dict(ORDER_PAYLOAD)
    if color is not None:
        payload['color'] = color
    return requests.post(Urls.BASE_URL + Urls.CREATE_ORDER, json=payload)


def get_order_id_by_track(track):
    """Возвращает id заказа по его трек-номеру."""
    response = requests.get(
        Urls.BASE_URL + Urls.GET_ORDER_BY_TRACK, params={'t': track}
    )
    return response.json()['order']['id']
