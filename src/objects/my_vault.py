from ansible_vault import Vault


class MyVault(object):
    def __init__(self):
        print("init Vault")

    def load_raw(self, file) -> str:
        vault = Vault('test')
        return vault.load(open('foo.yml').read())

    def dump_raw(self, text, stream=None):
        encrypted = self.vault.encrypt(text)
        if stream:
            stream.write(encrypted)
        else:
            return encrypted
