from DeezerApiTools import *
from Album import *


def albumLookup():
    string = input("Enter ID or link: ")
    id = ""
    try:
        id = parseId(string)
    except InvalidInputException:
        print("Try again.")
        albumLookup()
    a = Album(id)
    a.print()


def promptMode():
    mode = ""
    while mode.lower() not in ["s", "i"]:
        mode = input("Lookup by album ID [I], or search [S]: ")
    if mode.lower() == "i":
        albumLookup()


promptMode()
