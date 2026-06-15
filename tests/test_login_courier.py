import allure

from data import CourierMessages
from helper import generate_courier_data, login_courier


@allure.epic('Курьер')
@allure.feature('Авторизация курьера')
class TestLoginCourier:

    @allure.title('Курьер может авторизоваться: статус 200 и в ответе есть id')
    def test_courier_can_login(self, courier):
        response = login_courier(courier['login'], courier['password'])

        assert response.status_code == 200
        assert 'id' in response.json()

    @allure.title('Успешная авторизация возвращает id курьера')
    def test_login_returns_id(self, courier):
        response = login_courier(courier['login'], courier['password'])

        assert response.status_code == 200
        assert isinstance(response.json()['id'], int)

    @allure.title('Авторизация с неверным паролем возвращает ошибку 404')
    def test_login_with_wrong_password_returns_error(self, courier):
        response = login_courier(courier['login'], 'wrong_password')

        assert response.status_code == 404
        assert response.json()['message'] == CourierMessages.ACCOUNT_NOT_FOUND

    @allure.title('Авторизация с неверным логином возвращает ошибку 404')
    def test_login_with_wrong_login_returns_error(self, courier):
        response = login_courier('wrong_login', courier['password'])

        assert response.status_code == 404
        assert response.json()['message'] == CourierMessages.ACCOUNT_NOT_FOUND

    @allure.title('Авторизация без поля login возвращает ошибку 400')
    def test_login_without_login_returns_error(self, courier):
        response = login_courier('', courier['password'])

        assert response.status_code == 400
        assert response.json()['message'] == CourierMessages.NOT_ENOUGH_DATA_TO_LOGIN

    @allure.title('Авторизация без поля password возвращает ошибку')
    def test_login_without_password_returns_error(self, courier):
        response = login_courier(courier['login'], '')

        # При отсутствии пароля сервис возвращает ошибку (не 200).
        assert response.status_code != 200
        assert 'id' not in response.text

    @allure.title('Авторизация под несуществующим пользователем возвращает ошибку 404')
    def test_login_nonexistent_courier_returns_error(self):
        data = generate_courier_data()

        response = login_courier(data['login'], data['password'])

        assert response.status_code == 404
        assert response.json()['message'] == CourierMessages.ACCOUNT_NOT_FOUND
