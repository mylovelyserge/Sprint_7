import pytest
import requests

from data import Urls
from helper import (
    create_order,
    delete_courier,
    generate_courier_data,
    get_courier_id,
    get_order_id_by_track,
)


@pytest.fixture
def courier():
    """Создаёт курьера перед тестом и удаляет его после.

    Возвращает словарь с данными курьера и его id.
    Тестовые данные создаются перед тестом и удаляются после.
    """
    data = generate_courier_data()
    requests.post(Urls.BASE_URL + Urls.CREATE_COURIER, data=data)
    courier_id = get_courier_id(data['login'], data['password'])
    data['id'] = courier_id

    yield data

    # Чистим за собой. Курьер мог быть уже удалён в самом тесте.
    if courier_id is not None:
        delete_courier(courier_id)


@pytest.fixture
def courier_cleanup():
    """Собирает данные курьеров, созданных внутри теста, и удаляет их после.

    Тест добавляет в список словари вида {'login': ..., 'password': ...}.
    """
    created = []

    yield created

    for item in created:
        courier_id = get_courier_id(item['login'], item['password'])
        if courier_id is not None:
            delete_courier(courier_id)


@pytest.fixture
def order_track():
    """Создаёт заказ перед тестом и возвращает его трек-номер."""
    response = create_order(color=['BLACK'])
    return response.json()['track']


@pytest.fixture
def order_id(order_track):
    """Возвращает id созданного заказа."""
    return get_order_id_by_track(order_track)
