from extra import data
from extra import const
import pytest
import requests
import allure

class TestCreateUser:
    @allure.title('Cоздание нового пользователя')
    def test_create_new_user(self):
        with allure.step('Подготовка  тестовых данных'):
            payload = {"name": data.username_random, "email": data.email_random, "password": data.password_random}
        with allure.step('Отправка запроса'):
            response = requests.post(const.BASE_URL + const.CREATE_USER_HANDLE, data=payload)
            token = response.json()['accessToken']
        with allure.step('Проверка полученного статус-кода'):
            assert response.status_code == 200
        with allure.step('Удаление пользователя'):
            delete_response = requests.delete(const.BASE_URL + const.DELETE_USER_HANDLE,headers={'Authorization': token})
        with allure.step('Проверка полученного статус-кода'):
            assert delete_response.status_code in [200, 202]

    @allure.title('Cоздание уже существующего пользователя')
    def test_create_same_user(self):
        with allure.step('Подготовка  тестовых данных'):
            payload = {"Имя": data.username_registered, "Email": data.email_registered, "Пароль": data.password_registered}
        with allure.step('Отправка запроса'):
            response = requests.post(const.BASE_URL + const.CREATE_USER_HANDLE, data=payload)
        with allure.step('Проверка полученного статус-кода'):
            assert response.status_code == 403

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
            payload = {"Имя": username, "Email": email, "Пароль": password}
        with allure.step('Отправка запроса'):
            response = requests.post(const.BASE_URL + const.CREATE_USER_HANDLE, data=payload)
        with allure.step('Проверка полученного статус-кода'):
            assert response.status_code == 403
