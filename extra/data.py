import random
import string 

username_random = ''.join(random.choices(string.ascii_lowercase, k=5))
email_random = ''.join(random.choices(string.ascii_lowercase, k=5))+'@yandex.ru'
password_random = str(random.randint(100000, 900000))

username_registered = 'Alexandra'
email_registered = 'belova@yandex.ru'
password_registered = '123456'

ingr = ['61c0c5a71d1f82001bdaaa6d', '61c0c5a71d1f82001bdaaa6f']
wrong_hash_ingr = '60d3b41hfuacab0026a733c6'

