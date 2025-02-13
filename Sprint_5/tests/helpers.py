import random
import string

def generate_unique_email():

    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

    unique_email = f"user_{random_string}@yandex.ru"
    return unique_email
