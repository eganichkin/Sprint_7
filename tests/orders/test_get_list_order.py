import allure


class TestGetListOrder:

    @allure.title('Проверка, что в тело ответа возвращается список заказов.')
    @allure.description('Получение списка заказов у метро ["1", "2"], проверка получения статуса кода 200 и списка '
                        'заказов в теле ответа длиной > 0.')
    def test_get_list_order(self, order_methods):
        response = order_methods.get_list_orders()
        assert response.status_code == 200 and len(response.json()["orders"]) > 0
