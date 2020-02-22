
class Alias:

    def __init__(self, alias, command, description="none"):
        if not (alias or command):
            raise Exception("alias and command are mandatory")
        self.alias = alias
        self.cmd = cmd
        self.description = description

    def get_presentable_format(self):
        pass