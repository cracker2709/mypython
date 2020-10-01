from objects.MainObject import MainObject


class ClientObject(MainObject):
    def __init__(self) -> str:
        print("init client")

    def do_process(self) -> str:
        self.i += 2
        return f'<client call> --> {self.i}'
