import allure
import requests

from data import Urls, CourierMessages
from helper import generate_courier_data


@allure.epic('Курьер')
@allure.feature('Создание курьера')
class TestCreateCourier:

    @allure.title('Курьера можно создать: статус 201 и тело ok=true')
    def test_create_courier_success(self, courier_cleanup):
        data = generate_courier_data()
        courier_cleanup.append(data)

        response = requests.post(Urls.BASE_URL + Urls.CREATE_COURIER, data=data)

        assert response.status_code == 201
        assert response.json() == {'ok': True}

    @allure.title('Нельзя создать двух одинаковых курьеров: статус 409')
    def test_create_two_identical_couriers_returns_error(self, courier_cleanup):
        data = generate_courier_data()
        courier_cleanup.append(data)
        requests.post(Urls.BASE_URL + Urls.CREATE_COURIER, data=data)

        response = requests.post(Urls.BASE_URL + Urls.CREATE_COURIER, data=data)

        assert response.status_code == 409
        assert response.json()['message'] == CourierMessages.LOGIN_ALREADY_USED

    @allure.title('Можно создать курьера, передав все обязательные поля')
    def test_create_courier_with_required_fields(self, courier_cleanup):
        data = generate_courier_data()
        courier_cleanup.append(data)

        response = requests.post(Urls.BASE_URL + Urls.CREATE_COURIER, data=data)

        assert response.status_code == 201
        assert response.json() == {'ok': True}

    @allure.title('Если нет поля login — запрос возвращает ошибку 400')
    def test_create_courier_without_login_returns_error(self):
        data = generate_courier_data()
        del data['login']

        response = requests.post(Urls.BASE_URL + Urls.CREATE_COURIER, data=data)

        assert response.status_code == 400
        assert response.json()['message'] == CourierMessages.NOT_ENOUGH_DATA_TO_CREATE

    @allure.title('Если нет поля password — запрос возвращает ошибку 400')
    def test_create_courier_without_password_returns_error(self):
        data = generate_courier_data()
        del data['password']

        response = requests.post(Urls.BASE_URL + Urls.CREATE_COURIER, data=data)

        assert response.status_code == 400
        assert response.json()['message'] == CourierMessages.NOT_ENOUGH_DATA_TO_CREATE

    @allure.title('Создание курьера с уже существующим логином возвращает ошибку 409')
    def test_create_courier_with_existing_login_returns_error(self, courier_cleanup):
        data = generate_courier_data()
        courier_cleanup.append(data)
        requests.post(Urls.BASE_URL + Urls.CREATE_COURIER, data=data)

        # Тот же логин, но другие пароль и имя.
        duplicate = generate_courier_data()
        duplicate['login'] = data['login']

        response = requests.post(Urls.BASE_URL + Urls.CREATE_COURIER, data=duplicate)

        assert response.status_code == 409
        assert response.json()['message'] == CourierMessages.LOGIN_ALREADY_USED
