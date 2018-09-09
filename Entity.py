class Entity:

    def __init__(self, id):
        self.id = str(id)

    def load(self):
        raise NotImplementedError

    def _constructDeezerApiUrl(self):
        raise NotImplementedError

    def _getDeezerResponse(self):
        raise NotImplementedError
