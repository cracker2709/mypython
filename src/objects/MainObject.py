class MainObject(object):
    """A simple example class"""
    i = 0

    def __init__(self):
        print("init master")

    def do_process(self) -> str:
        self.i += 1
        return f'[main call] --> {self.i}'
