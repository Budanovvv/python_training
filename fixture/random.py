import random
import string


class RandomHelper:

    def __init__(self, app):
        self.app = app

    def rnd_string(self, maxlen):
        symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
        return self + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])