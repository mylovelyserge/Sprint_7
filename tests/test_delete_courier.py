import allure

from data import CourierMessages
from helper import delete_courier


@allure.epic('Курьер')
@allure.feature('Удаление курьера')
class TestDeleteCourier:

    @allure.title('Успешное удаление курьера: статус 200 и тело ok=true')
    def test_delete_courier_success(self, courier):
        response = delete_courier(courier['id'])

        assert response.status_code == 200
        assert response.json() == {'ok': True}

    @allure.title('Удаление с несуществующим id возвращает ошибку 404')
    def test_delete_courier_with_nonexistent_id_returns_error(self):
        response = delete_courier(0)

        assert response.status_code == 404
        assert response.json()['message'] == CourierMessages.COURIER_NOT_FOUND

    @allure.title('Удаление без id возвращает ошибку')
    def test_delete_courier_without_id_returns_error(self):
        response = delete_courier('')

        assert response.status_code == 404
