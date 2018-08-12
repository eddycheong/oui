import os
from .parser import parser

__database = None
__ouiFilePath = os.path.abspath(os.path.join(__file__, os.pardir)) + "\\oui.csv"

# Private methods for this module
def __normalizeOui(oui):
    pass

def __seed():
    update()

# Public methods for this module
def update():
    global __database
    __database = parser(__ouiFilePath)

def lookup(oui):
    return __database[oui]["name"]

if __name__ == "__main__":
    __seed()
    print("Ran as script " + __name__)
else:
    __seed()