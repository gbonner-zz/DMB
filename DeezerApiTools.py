import json


def constructDeezerApiUrl(type, id):
    return 'https://api.deezer.com/' + type + '/' + id


def loadResponse(jsonBlob):
    return json.loads(jsonBlob)
