import string
import random

def random_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32))