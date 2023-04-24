from typing import BinaryIO
from .u_tools import *


class Script:

    def __init__(self, cmds=None):
        if cmds is None:
            self.cmds = []
        else:
            self.cmds = cmds


    @classmethod
    def parse(cls, stream: BinaryIO):
        script_len = read_varint(stream=stream)

        cmds = stream.read(script_len)

        return cls(cmds)


if __name__ == "__main__":
    pass