from objects.MainObject import MainObject


class ServerObject(MainObject):

    def __init__(self) -> str:
        print("init server")

    def do_process(self) -> str:
        res = super(ServerObject, self).do_process()
        self.i += 2
        return res + f' <<server call>> --> {self.i}'
