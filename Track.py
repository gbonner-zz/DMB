import requests
from DMB.Entity import Entity
from DMB.DeezerApiTools import *


class Track(Entity):

    def __init__(self, id):
        super(Track, self).__init__(id)
        self.isrc, self.duration, self.explicit, self.artist, self.position, self.title = [None] * 6
        self.isLoaded = False
        self._response = None

    def load(self):
        apiRequest = requests.get(self.constructDeezerApiUrl())
        j = loadResponse(apiRequest.content)
        self.isLoaded = True
        self.isrc = j['isrc']
        self.duration = j['duration']
        self.explicit = bool(j['explicit_lyrics'])
        self.artist = j['artist']
        self.position = j['track_position']
        self.title = j['title']

    def print(self):
        print(str(self.position) + '\t' + self.isrc + '\t' + self.timeAsMinuteString() + '\t' + self.title)

    def timeAsMinuteString(self):
        min = int(self.duration / 60)
        sec = self.duration % 60
        if sec < 10:
            sec = '0' + str(sec)
        return str(min) + ':' + str(sec)

    def constructDeezerApiUrl(self):
        return 'http://api.deezer.com/track/' + self.id
