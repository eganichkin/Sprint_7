import allure
import pytest


class TestLoginCourier:
    @allure.title('Проверка, что курьер может авторизоваться, запрос возвращает id.')
    @allure.description('Создание курьера; логирование и проверка получения статуса кода 200 и id>0; удаление курьера.')
    def test_login_courier(self, courier_methods, courier):
        response = courier_methods.post_login_courier()
        courier_methods.courier_id = response.json()['id']
        assert response.status_code == 200 and response.json()['id'] > 0

    @allure.title('Проверка, что для авторизации курьера необходимо заполнить все обязательные поля.')
    @allure.description('Создание курьера; обнуление одного из обязательных полей, попытка логирования и проверка '
                        'получения статуса кода 400 и сообщения об ошибке; удаление курьера.')
    @pytest.mark.parametrize(
        'empty_field_name',
        ["login", "password"]
    )
    def test_login_courier_with_empty_login_pass(self, courier_methods, empty_field_name):
        courier_methods.courier_data[empty_field_name] = ''
        response = courier_methods.post_login_courier()
        assert (response.status_code == 400
                and response.json()['message'] == 'Недостаточно данных для входа')

    @allure.title('Проверка, что при авторизации курьера проводитя проверка корректности всех обязательных полей.')
    @allure.description('Создание курьера; изменение одного из обязательных полей, попытка логирования и проверка '
                        'получения статуса кода 404 и сообщения об ошибке; удаление курьера.')
    @pytest.mark.parametrize(
        'empty_field_name',
        ["login", "password"]
    )
    def test_login_courier_with_incorrect_login_pass(self, courier_methods, empty_field_name):
        courier_methods.courier_data[empty_field_name] = 'IncorrectValue'
        response = courier_methods.post_login_courier()
        assert response.status_code == 404 and response.json()['message'] == 'Учетная запись не найдена'
