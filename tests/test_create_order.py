import allure
import pytest

from helper import create_order


@allure.epic('Заказ')
@allure.feature('Создание заказа')
class TestCreateOrder:

    @allure.title('Создание заказа с цветом: {color}')
    @pytest.mark.parametrize(
        'color',
        [
            ['BLACK'],
            ['GREY'],
            ['BLACK', 'GREY'],
            [],
        ],
        ids=['black', 'grey', 'black_and_grey', 'no_color'],
    )
    def test_create_order_with_colors(self, color):
        response = create_order(color=color)

        assert response.status_code == 201
        assert 'track' in response.json()
