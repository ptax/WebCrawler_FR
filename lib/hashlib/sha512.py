import hashlib


class sha512:

    def make(self, *args):
        result = list(map(lambda x: (hashlib.sha512(x).hexdigest(), args)))
        return '_'.join(result)