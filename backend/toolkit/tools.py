from flask import Response, Request
import random
import string

def get_random_str():
    """Returns a random long string used to identify a user when not logging"""
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(64))