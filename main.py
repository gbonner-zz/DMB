from DeezerApiTools import *
from Album import *


def albumLookup():
    string = input("Enter ID or link: ")
    id: str = ""
    try:
        id = parseId(string)
    except InvalidInputException:
        print("Try again.")
        albumLookup()
    a = Album(id)
    a.print()


def promptMode():
    mode = ""
    albumLookup()

promptMode()
