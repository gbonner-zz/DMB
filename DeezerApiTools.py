import json
import re

NUMBER_ONLY = '^[0-9]+$'
LINK_EXTRACT = 'https*:\/\/[a-z]*\.deezer\.com[\/a-z]+\/([0-9]+)$'


class InvalidInputException(Exception):
    def __init__(self, message=""):
        self.message = message

def constructDeezerApiUrl(type, id):
    return 'https://api.deezer.com/' + type + '/' + id


def loadResponse(jsonBlob):
    return json.loads(jsonBlob)


def parseId(id):
    if isinstance(id, int):
        return str(id)
    if isinstance(id, str):
        if re.search(NUMBER_ONLY, id.lower()):
            return id
        elif re.match(LINK_EXTRACT, id.lower()):
            return re.match(LINK_EXTRACT, id.lower())[1]
        else:
            raise InvalidInputException
