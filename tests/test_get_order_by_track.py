import allure
import requests

from data import Urls, OrderMessages


@allure.epic('Заказ')
@allure.feature('Получить заказ по его номеру')
class TestGetOrderByTrack:

    @allure.title('Успешный запрос возвращает объект с заказом')
    def test_get_order_by_track_success(self, order_track):
        response = requests.get(
            Urls.BASE_URL + Urls.GET_ORDER_BY_TRACK,
            params={'t': order_track},
        )

        assert response.status_code == 200
        assert response.json()['order']['track'] == order_track

    @allure.title('Запрос без номера заказа возвращает ошибку 400')
    def test_get_order_without_track_returns_error(self):
        response = requests.get(Urls.BASE_URL + Urls.GET_ORDER_BY_TRACK)

        assert response.status_code == 400
        assert response.json()['message'] == OrderMessages.NOT_ENOUGH_DATA_TO_SEARCH

    @allure.title('Запрос с несуществующим номером заказа возвращает ошибку 404')
    def test_get_order_with_nonexistent_track_returns_error(self):
        response = requests.get(
            Urls.BASE_URL + Urls.GET_ORDER_BY_TRACK,
            params={'t': 0},
        )

        assert response.status_code == 404
        assert response.json()['message'] == OrderMessages.ORDER_NOT_FOUND
