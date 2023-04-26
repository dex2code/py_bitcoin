from typing import BinaryIO
from .u_tools import *
from .op import *


class Script:

    def __init__(self, cmds=None):
        if cmds is None:
            self.cmds = []
        else:
            self.cmds = cmds
    

    def __repr__(self):
        result = []

        for cmd in self.cmds:
            if type(cmd) == int:
                if cmd in OP_CODE:
                    op_name = OP_CODE.get(cmd)['name']
                else:
                    op_name = f"OP_{cmd}"
                result.append(op_name)
            else:
                result.append(cmd.hex())

        return ' '.join(result)
    

    def __add__(self, __value):
        return self.__class__(cmds=(self.cmds + __value.cmds))


    @classmethod
    def parse(cls, stream: BinaryIO):
        cmds = []
        count = 0

        script_len = read_varint(stream=stream)

        while count < script_len:
            current_byte = stream.read(1)
            count += 1

            current_int = le_to_int(input_bytes=current_byte)

            if current_int >= 1 and current_int <= 75:
                n = current_int
                b = stream.read(n)
                count += n

                cmds.append(b)

            elif current_int == 76:
                b = stream.read(1)
                count += 1

                n = le_to_int(input_bytes=b)

                b = stream.read(n)
                count += n

                cmds.append(b)

            elif current_int == 77:
                b = stream.read(2)
                count += 2

                n = le_to_int(input_bytes=b)

                b = stream.read(n)
                count += n

                cmds.append(b)

            else:
                op_code = current_int
                cmds.append(op_code)

        if count != script_len:
            raise SyntaxError("Script parse error")
            
        return cls(cmds)
    

    def serialize(self) -> bytes:
        result = b''

        for cmd in self.cmds:
            if type(cmd) == int:
                result += int_to_le(input_int=cmd, output_length=1)
            else:
                cmd_length = len(cmd)
            
                if cmd_length >=1 and cmd_length <= 75:
                    result += int_to_le(input_int=cmd_length, output_length=1)
                
                elif cmd_length >=76 and cmd_length <=255:
                    result += int_to_le(input_int=76, output_length=1)
                    result += int_to_le(input_int=cmd_length, output_length=1)
                
                elif cmd_length >= 256 and cmd_length <= 520:
                    result += int_to_le(input_int=77, output_length=1)
                    result += int_to_le(input_int=cmd_length, output_length=2)
                
                else:
                    raise ValueError(f"Wrong cmd length: {cmd_length}")
                
                result += cmd

        total = len(result)

        return encode_varint(i=total) + result
            

if __name__ == "__main__":
    pass