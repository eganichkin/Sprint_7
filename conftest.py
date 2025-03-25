import pytest
from methods.courier_methods import CourierMethods
from methods.order_methods import OrderMethods


@pytest.fixture()
def courier_methods():
    return CourierMethods()


@pytest.fixture()
def order_methods():
    return OrderMethods()


@pytest.fixture()
def courier(courier_methods):
    courier_methods.post_create_courier()
    yield
    courier_methods.delete_courier()
