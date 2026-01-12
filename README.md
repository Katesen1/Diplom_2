Были созданы тесты:
1. Создание пользователя - test_create_user.py
    1) создать уникального пользователя - test_create_new_user
    2) создать пользователя, который уже зарегистрирован - test_create_same_user
    3) создать пользователя и не заполнить одно из обязательных полей - test_without_field
2. Логин пользователя - test_login_user.py
    1) вход под существующим пользователем - test_login_user
    2) вход с неверным логином и паролем - test_login_wrong_data
3. Создание заказа - test_create_order.py
    1) с авторизацией и ингредиентами - test_with_auth
    2) без авторизации с ингредиентами - test_without_auth
    3) без ингредиентов - test_without_ingredients
    4) с неверным хешем ингредиентов - test_wrong_hash

