import allure
import pytest


class TestCreateCourier:

    @allure.title('Проверка, что курьера можно создать, успешный запрос возвращает "ok":true')
    @allure.description('Заполнение всех обязательных полей, создание курьера, проверка получения статуса кода 200 и '
                        'сообщения "ok":true.')
    def test_create_courier(self, courier_methods):
        response = courier_methods.post_create_courier()
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title('Проверка, что нельзя создать двух одинаковых курьеров.')
    @allure.description('Успешное создание одного курьера, попытка создания второго курьера с теми же учётными данными,'
                        'проверка получения статуса кода 409 и сообщения об ошибке.')
    def test_create_two_couriers(self, courier_methods):
        courier_methods.post_create_courier()
        response = courier_methods.post_create_courier()
        assert (response.status_code == 409
                and response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.')

    @allure.title('Проверка, что для создания курьера необходимо заполнить все обязательные поля.')
    @allure.description('Обнуление одного из обязательных полей, попытка создания курьера и проверка '
                        'получения статуса кода 400 и сообщения об ошибке.')
    @pytest.mark.parametrize(
        'empty_field_name',
        ["login", "password"]
    )
    def test_create_courier_with_empty_login_pass(self, courier_methods, empty_field_name):
        courier_methods.courier_data[empty_field_name] = ''
        response = courier_methods.post_create_courier()
        assert (response.status_code == 400
                and response.json()['message'] == 'Недостаточно данных для создания учетной записи')

    @allure.title('Проверка необязательности заполнения поля "firstname" при создании курьера.')
    @allure.description('Обнуление поля "firstname", попытка создания курьера, проверка получения статуса кода 200 и '
                        'сообщения "ok":true.')
    def test_create_courier_with_empty_firstname(self, courier_methods):
        courier_methods.courier_data["firstname"] = ''
        response = courier_methods.post_create_courier()
        assert response.status_code == 201 and response.text == '{"ok":true}'
