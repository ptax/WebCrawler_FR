import hashlib


class sha512:

    def make(self, *args):
        result = list(map(lambda x: (hashlib.sha512(repr(x).encode('utf-8')).hexdigest()), args))
        return '_'.join(result)