import random
import string


def get_random_password() -> str:
    chars = set(string.ascii_uppercase + string.ascii_lowercase + string.digits)
    password = []
    password += random.sample(chars, 8)
    ready_password = ''.join(password)
    return ready_password


print(get_random_password())
