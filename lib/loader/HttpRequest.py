import urllib.request as loader_lib


class HttpRequest:

    @staticmethod
    def load(url, headers=None):
        answer = ''
        req = loader_lib.Request(url, headers=headers)
        with loader_lib.urlopen(req) as response:
            answer = response.read()
        return answer, response.getcode()
