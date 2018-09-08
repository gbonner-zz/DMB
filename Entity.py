class Entity:

    def __init__(self, id):
        self.id = str(id)

    def load(self):
        raise NotImplementedError

    def constructDeezerApiUrl(self):
        raise NotImplementedError

    def getDeezerResponse(self):
        raise NotImplementedError
