from . import base

class NERextract(base.Base):
    def __init__(self, service_uri, api_key):
        super().__init__(service_uri, api_key)
        self._type = 'NER'