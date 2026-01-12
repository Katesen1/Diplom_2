from extra import data
from extra import const
import pytest
import requests
import allure

class TestLoginUser:
    @allure.title('Вход под существующим пользователем')
    def test_login_user(self):
        with allure.step('Подготовка тестовых данных'):
            payload = {"email": data.email_registered, "password": data.password_registered}
        with allure.step('Отправка запроса'):
            response = requests.post(const.BASE_URL + const.LOGIN_USER_HANDLE, data=payload)
        with allure.step('Проверка полученного статус-кода'):
            assert response.status_code == 200

    @pytest.mark.parametrize(
        "email, password",
        [
            pytest.param(data.email_random, data.email_registered, id='random email'),
            pytest.param(data.email_registered, data.password_random, id='random password'),
        ],
    )
    @allure.title('Вход с неверными данными')
    def test_login_wrong_data(self, email, password):
        with allure.step('Подготовка тестовых данных'):
            payload = {"Email": email, "Пароль": password}
        with allure.step('Отправка запроса'):    
            response = requests.post(const.BASE_URL + const.LOGIN_USER_HANDLE, data=payload)
        with allure.step('Проверка полученного статус-кода'):
            assert response.status_code == 401
