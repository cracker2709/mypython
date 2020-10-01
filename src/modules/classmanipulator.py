from objects.MainObject import MainObject
from objects.ClientObject import ClientObject
from objects.ServerObject import ServerObject


def play_with_classes():
    m = MainObject()
    c = ClientObject()
    s = ServerObject()

    obj = [m, c, s]

    for o in obj:
        print(o.do_process())
