import allure
import requests

from data import Urls, OrderMessages


@allure.epic('Заказ')
@allure.feature('Принять заказ')
class TestAcceptOrder:

    @allure.title('Успешное принятие заказа: статус 200 и тело ok=true')
    def test_accept_order_success(self, courier, order_id):
        response = requests.put(
            Urls.BASE_URL + Urls.ACCEPT_ORDER.format(id=order_id),
            params={'courierId': courier['id']},
        )

        assert response.status_code == 200
        assert response.json() == {'ok': True}

    @allure.title('Принятие заказа без id курьера возвращает ошибку 400')
    def test_accept_order_without_courier_id_returns_error(self, order_id):
        response = requests.put(
            Urls.BASE_URL + Urls.ACCEPT_ORDER.format(id=order_id)
        )

        assert response.status_code == 400
        assert response.json()['message'] == OrderMessages.NOT_ENOUGH_DATA_TO_SEARCH

    @allure.title('Принятие заказа с неверным id курьера возвращает ошибку 404')
    def test_accept_order_with_wrong_courier_id_returns_error(self, order_id):
        response = requests.put(
            Urls.BASE_URL + Urls.ACCEPT_ORDER.format(id=order_id),
            params={'courierId': 999999999},
        )

        assert response.status_code == 404
        assert response.json()['message'] == OrderMessages.COURIER_NOT_EXISTS

    @allure.title('Принятие заказа без id заказа возвращает ошибку')
    def test_accept_order_without_order_id_returns_error(self, courier):
        response = requests.put(
            Urls.BASE_URL + Urls.ACCEPT_ORDER.format(id=''),
            params={'courierId': courier['id']},
        )

        assert response.status_code == 404

    @allure.title('Принятие заказа с неверным id заказа возвращает ошибку 404')
    def test_accept_order_with_wrong_order_id_returns_error(self, courier):
        response = requests.put(
            Urls.BASE_URL + Urls.ACCEPT_ORDER.format(id=999999999),
            params={'courierId': courier['id']},
        )

        assert response.status_code == 404
        assert response.json()['message'] == OrderMessages.ORDER_NOT_EXISTS
