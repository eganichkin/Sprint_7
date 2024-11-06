import allure
import pytest


class TestCreateOrder:
    @allure.title('Проверка создания заказа с различными вариантами заполения полa "color".')
    @allure.description('Заполнение параметров заказа корректными данными, поле "color" записать значениями из '
                        'параметризации; проверка получения статуса кода 200 и значения "track" в теле ответа > 0.')
    @pytest.mark.parametrize(
        'color',
        (['BLACK'], ['GREY'], ['BLACK', 'GREY'], [])
    )
    def test_create_order_with_different_color(self, order_methods, color):
        order_methods.order_data["color"] = color
        response = order_methods.post_create_order()
        assert response.status_code == 201 and response.json()['track'] > 0
