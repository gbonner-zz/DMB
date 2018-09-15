class Entity:

    def __init__(self, id: str):
        self.id = str(id)

    def load(self):
        raise NotImplementedError

    def _getDeezerResponse(self):
        raise NotImplementedError

    def _getiTunesRepsone(self):
        raise NotImplementedError
