import hashlib
from json import dumps as json_dumps

import base58


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


from . import S256_A, S256_B, S256_N, S256_Gx, S256_Gy
from .fields import S256_FieldElement


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
                return b'\x02' + self.x.num.to_bytes(32, "big")
            else:
                return b'\x03' + self.x.num.to_bytes(32, "big")
        else:
            return b'\x04' + self.x.num.to_bytes(32, "big") + self.y.num.to_bytes(32, "big")


    def address_value(self, compressed: bool = True, testnet: bool = False) -> bytes:
        h160 = hashlib.new(
            name="ripemd160",
            data=hashlib.sha256(string=self.sec_value(compressed=compressed)).digest()
        ).digest()

        if testnet:
            prefix = b'\x6f'
        else:
            prefix = b'\x00'

        result = prefix + h160

        return base58.b58encode_check(v=result)

if __name__ == "__main__":
    pass