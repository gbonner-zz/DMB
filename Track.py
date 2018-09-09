import requests
from Entity import Entity
from DeezerApiTools import *


class Track(Entity):

    def __init__(self, id):
        super().__init__(id)
        self.isrc, self.duration, self.explicit, self.artist, self.position, self.title = [None] * 6
        self.isLoaded = False
        self._response = None

    def load(self):
        self._getDeezerResponse()
        self.isLoaded = True
        self.isrc = self._response['isrc']
        self.duration = self._response['duration']
        self.explicit = bool(self._response['explicit_lyrics'])
        self.artist = self._response['artist']
        self.position = self._response['track_position']
        self.title = self._response['title']

    def print(self):
        print(str(self.position) + '\t' + self.isrc + '\t' + self.timeAsMinuteString() + '\t' + self.title)

    def timeAsMinuteString(self):
        min = int(self.duration / 60)
        sec = self.duration % 60
        if sec < 10:
            sec = '0' + str(sec)
        return str(min) + ':' + str(sec)

    def _constructDeezerApiUrl(self):
        return 'http://api.deezer.com/track/' + self.id

    def _getDeezerResponse(self):
        url = 'http://api.deezer.com/track/' + self.id
        rawResponse = requests.get(url).content
        self._response = loadResponse(rawResponse)
