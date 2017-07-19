import re
import html

class Parser:

    def __init__(self, content):
        self.content = content

    def as_dictionary(self):
        pass

    def replace_html(self, content):
        result = re.sub('<[^>]*>', ' ', content)
        result = html.unescape(result)
        result = re.sub('\s+', ' ', result)
        return result.strip()