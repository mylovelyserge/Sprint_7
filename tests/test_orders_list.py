import allure
import requests

from data import Urls


@allure.epic('Заказ')
@allure.feature('Список заказов')
class TestOrdersList:

    @allure.title('В теле ответа возвращается список заказов')
    def test_get_orders_returns_list(self):
        response = requests.get(Urls.BASE_URL + Urls.GET_ORDERS)

        assert response.status_code == 200
        assert isinstance(response.json()['orders'], list)

    @allure.title('Список заказов не пустой')
    def test_orders_list_is_not_empty(self):
        response = requests.get(Urls.BASE_URL + Urls.GET_ORDERS)

        assert response.status_code == 200
        assert len(response.json()['orders']) > 0
