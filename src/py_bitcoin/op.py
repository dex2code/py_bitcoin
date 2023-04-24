from .u_tools import *


# 97 == 0x61
def op_nop(stack: list) -> bool:
    return True


# 118 == 0x76
def op_dup(stack: list) -> bool:
    if len(stack) < 1:
        return False
    else:
        stack.append(stack[-1])
        return True


# 169 == 0xa9
def op_hash160(stack: list) -> bool:
    if len(stack) < 1:
        return False
    else:
        element = stack.pop()
        stack.append(get_hash160(message=element, to_int=False))
        return True


# 170 == 0xaa
def op_hash256(stack: list) -> bool:
    if len(stack) < 1:
        return False
    else:
        element = stack.pop()
        stack.append(get_hash256(message=element, to_int=False))
        return True


OP_CODE = {
    97:  {'func': 'op_nop', 'name': 'OP_NOP'},
    118: {'func': 'op_dup', 'name': 'OP_DUP'},
    169: {'func': 'op_hash160', 'name': 'OP_HASH160'},
    170: {'func': 'op_hash256', 'name': 'OP_HASH256'}
}


if __name__ == "__main__":
    pass
