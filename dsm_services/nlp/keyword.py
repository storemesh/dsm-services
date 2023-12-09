from . import base

class KeywordExtract(base.Base):
    def __init__(self, service_uri, api_key):
        super().__init__(service_uri, api_key)
        self._type = 'KEYWORD'