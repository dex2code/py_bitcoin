from json import dumps as json_dumps

import base58

from . import *
from .fields import S256_FieldElement
from .u_tools import *


class Point:

    def __init__(self, x, y, a, b) -> None:
        self.x = x
        self.y = y
        self.a = a
        self.b = b

        if (self.x is None) and (self.y is None):
            return
        
        if y**2 != x**3 + (a * x) + b:
            raise ValueError(f"Point ({x}, {y}) is not on the curve 'x**3 + {a}*x + {b}'")


    def __repr__(self) -> str:
        if (self.x is None) and (self.y is None):
            return f"P_(I) on 'x**3 + {self.a}*x + {self.b}'"

        return f"P_({self.x}, {self.y}) on 'x**3 + {self.a}*x + {self.b}'"


    def __eq__(self, __value) -> bool:
        return (self.x == __value.x) and (self.y == __value.y) and (self.a == __value.a) and (self.b == __value.b)


    def __ne__(self, __value) -> bool:
        return not (self == __value)


    def __add__(self, __value) -> object:
        if (self.a != __value.a) or (self.b != __value.b):
            raise TypeError(f"Given points ('{self}' and '{__value}') aren't on the same curve!")
        
        if (self.x is None) and (self.y is None): # I + A = A
            return __value

        if (__value.x is None) and (__value.y is None): # A + I = A
            return self

        if self.x == __value.x: # Bot points are on the same X
            if self.y == __value.y: # Bot points are on the same Y
                if (self.y == 0 * self.x): # Both poins have Y == 0
                    return self.__class__(x=None, y=None, a=self.a, b=self.b)
                else: # A + A = B
                    s = (3 * self.x**2 + self.a) / (2 * self.y)
            else: # A + (-A) = I
                return self.__class__(x=None, y=None, a=self.a, b=self.b)
        else: # A + B = C
            s = (__value.y - self.y) / (__value.x - self.x)

        new_x = s**2 - self.x - __value.x
        new_y = s * (self.x - new_x) - self.y

        return self.__class__(x=new_x, y=new_y, a=self.a, b=self.b)


    def __rmul__(self, __value) -> object:
        coeff = __value
        current = self
        result = self.__class__(x=None, y=None, a=self.a, b=self.b)

        while coeff:
            if coeff & 1:
                result = result + current

            current = current + current
            coeff >>= 1

        return result


class S256_Point(Point):

    def __init__(self, x, y, a=None, b=None) -> None:
        if type(x) == int:
            super().__init__(x=S256_FieldElement(x), y=S256_FieldElement(y), a=S256_FieldElement(S256_A), b=S256_FieldElement(S256_B))
        else:
            super().__init__(x=x, y=y, a=S256_FieldElement(S256_A), b=S256_FieldElement(S256_B))


    def __repr__(self) -> str:
        my_repr = {
            "x": {
                "int": self.x.num,
                "hex": "0x"+"{:x}".format(self.x.num).zfill(64)
            },
            "y": {
                "int": self.y.num,
                "hex": "0x"+"{:x}".format(self.y.num).zfill(64)
            }
        }

        return json_dumps(obj=my_repr, indent=4)


    def __rmul__(self, __value) -> object:
        coeff = __value % S256_N
        
        return super().__rmul__(coeff)
    

    def sec_value(self, compressed: bool = True) -> bytes:
        """Returns public key in SEC format"""
        if compressed:
            if self.y.num % 2 == 0:
                return b'\x02' + int_to_be(input_int=self.x.num)
            else:
                return b'\x03' + int_to_be(input_int=self.x.num)
        else:
            return b'\x04' + int_to_be(input_int=self.x.num) + int_to_be(input_int=self.y.num)


    def address_value(self, compressed: bool = True, testnet: bool = False) -> bytes:
        h160 = get_hash160(message=self.sec_value(compressed=compressed))

        if testnet:
            prefix = b'\x6f'
        else:
            prefix = b'\x00'

        result = prefix + h160

        return base58.b58encode_check(v=result)
    

    @classmethod
    def restore_from_sec(self, sec_bytes: bytes):
        if sec_bytes[0] == 4:
            x = be_to_int(input_bytes=sec_bytes[1:33])
            y = be_to_int(input_bytes=sec_bytes[33:65])
            return S256_Point(x=x, y=y)
        
        is_even = sec_bytes[0] == 2

        num = be_to_int(input_bytes=sec_bytes[1:])
        x = S256_FieldElement(num=num)

        alpha = x**3 + S256_FieldElement(num=S256_B)
        beta = alpha.get_sqrt()

        if beta.num % 2 == 0:
            even_beta = beta
            odd_beta = S256_FieldElement(num=(S256_PRIME - beta.num))
        else:
            even_beta = S256_FieldElement(num=(S256_PRIME - beta.num))
            odd_beta = beta
        
        if is_even:
            return S256_Point(x=x, y=even_beta)
        else:
            return S256_Point(x=x, y=odd_beta)


if __name__ == "__main__":
    pass