from extra import data
from extra import const
import pytest
import requests
import allure

class TestCreateUser:
    @allure.title('Cоздание нового пользователя')
    def test_create_new_user(self, delete_user):
        with allure.step('Подготовка  тестовых данных'):
            payload = {"name": data.username_random, "email": data.email_random, "password": data.password_random}
        with allure.step('Отправка запроса'):
            response = requests.post(const.BASE_URL + const.CREATE_USER_HANDLE, data=payload)
            response_data = response.json()
            token = response_data['accessToken']
            user_data = response_data['user']
            delete_user.append(token)
        with allure.step('Проверка полученного статус-кода и тела ответа'):
            assert response.status_code == 200 
            assert response_data['success'] == True
            assert 'accessToken' in response_data
            assert 'refreshToken' in response_data
            assert user_data['email'] == payload["email"]
            assert user_data['name'] == payload['name']
            
    @allure.title('Cоздание уже существующего пользователя')
    def test_create_same_user(self):
        with allure.step('Подготовка  тестовых данных'):
            payload = {"name": data.username_registered, "email": data.email_registered, "password": data.password_registered}
        with allure.step('Отправка запроса'):
            response = requests.post(const.BASE_URL + const.CREATE_USER_HANDLE, data=payload)
            response_data = response.json()
        with allure.step('Проверка полученного статус-кода и тела ответа'):
            assert response.status_code == 403
            assert response_data['success'] == False
            assert response_data['message'] == 'User already exists'
            
    @pytest.mark.parametrize(
        "username, email, password",
        [
            pytest.param("", data.email_random, data.password_random, id="without username"),
            pytest.param(data.username_random, "", data.password_random, id="without email"),
            pytest.param(data.username_random, data.email_random, "", id="without password"),
        ],
    )
    @allure.title('Cоздание пользователя с пустым полем')
    def test_without_field(self, username, email, password):
        with allure.step('Подготовка  тестовых данных'):
            payload = {"name": username, "email": email, "password": password}
        with allure.step('Отправка запроса'):
            response = requests.post(const.BASE_URL + const.CREATE_USER_HANDLE, data=payload)
            response_data = response.json()
        with allure.step('Проверка полученного статус-кода и тела ответа'):
            assert response.status_code == 403 
            assert response_data['success'] == False
            assert response_data['message'] == 'Email, password and name are required fields'