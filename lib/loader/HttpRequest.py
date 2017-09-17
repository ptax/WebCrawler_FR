import urllib.request as loader_lib
import ssl

class HttpRequest:

    @staticmethod
    def load(url, headers=None):
        answer = ''
        context = ssl._create_unverified_context()
        req = loader_lib.Request(url, headers=headers)
        with loader_lib.urlopen(req, context=context) as response:
            answer = response.read()
        return answer, response.getcode()
