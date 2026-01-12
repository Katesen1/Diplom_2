from extra import data
from extra import const
import requests
import allure

class TestCreateOrder:
    @allure.title('Cоздание заказа с авторизацией и ингредиентами')
    def test_with_auth(self):
        with allure.step('Подготовка тестовых данных для авторизации'):
            payload1 = {"email": data.email_registered, "password": data.password_registered}
        with allure.step('Отправка запроса на авторизацию'):
            response1 = requests.post(const.BASE_URL + const.LOGIN_USER_HANDLE, data=payload1)
        with allure.step('Проверка полученного статус-кода при авторизации'):
            assert response1.status_code == 200
        with allure.step('Подготовка тестовых данных для выбора ингредиентов'):
            payload2 = {'ingredients': data.ingr}
        with allure.step('Отправка запроса на создание заказа'):
            response2 = requests.post(const.BASE_URL+const.CREATE_ORDER_HANDLE, data=payload2)
        with allure.step('Проверка полученного статус-кода'):
            assert response2.status_code == 200
    
    @allure.title('Cоздание заказа без авторизации с ингредиентами')
    def test_without_auth(self):
        with allure.step('Подготовка тестовых данных для выбора ингредиентов'):
            payload = {'ingredients': data.ingr}
        with allure.step('Отправка запроса на создание заказа'):    
            response = requests.post(const.BASE_URL+const.CREATE_ORDER_HANDLE, data=payload)
        with allure.step('Проверка, что нас перекинуло за авторизацию'):
            assert response.status_code == 200
    
    @allure.title('Cоздание заказа без ингридиентов и авторизации')
    def test_without_ingredients(self):
        with allure.step('Отправка запроса на создание заказа без ингридиентов'): 
            response = requests.post(const.BASE_URL+const.CREATE_ORDER_HANDLE)
        with allure.step('Проверка полученного статус-кода'):
            assert response.status_code == 400
    
    @allure.title('Cоздание заказа с неверным хешем ингридиента без авторизации')
    def test_wrong_hash(self):
        with allure.step('Подготовка тестовых данных с неверным хешем ингридиента'):
            payload = {'ingredients': data.wrong_hash_ingr}
        with allure.step('Отправка запроса'):    
            response = requests.post(const.BASE_URL+const.CREATE_ORDER_HANDLE, data=payload)
        with allure.step('Проверка полученного статус-кода'):
            assert response.status_code == 500