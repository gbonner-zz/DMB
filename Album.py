from Entity import Entity
from Track import Track
from DeezerApiTools import *
import requests


class Album(Entity):

    def __init__(self, id):
        super().__init__(id)
        self.isLoaded = False
        self.id = str(id)
        self.artist = None
        self.tracks = None
        self.title = None
        self._response = None

    def load(self):
        self._getDeezerResponse()
        self.artist = self._response['contributors'][0]['name']
        self.title = self._response['title']
        self.tracks = []
        self.isLoaded = True
        for track in self._response['tracks']['data']:
            t = Track(track['id'])
            self.tracks.append(t)

    def loadTracks(self):
        if not self.isLoaded:
            print('Album is not loaded. Fetching tracklist.')
            self.load()
        for t in self.tracks:
            t.load()

    def print(self):
        self.loadTracks()
        print(self.title + ' - ' + self.artist)
        for t in self.tracks:
            t.print()

    def _getDeezerResponse(self):
        url = 'http://api.deezer.com/album/' + self.id
        rawResponse = requests.get(url).content
        self._response = loadResponse(rawResponse)


