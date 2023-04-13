import os, sys

parent = os.path.abspath('.')
sys.path.insert(1, parent)


from src.py_bitcoin.curves import Point, S256_Point
from src.py_bitcoin.fields import FieldElement, S256_Field

"""
prime = 223

x = FieldElement(num=15, prime=prime)
y = FieldElement(num=86, prime=prime)
a = FieldElement(num=0, prime=prime)
b = FieldElement(num=7, prime=prime)

pp = Point(x=x, y=y, a=a, b=b)
pc = pp
cc = 1
print(f"{cc} -- ({pc.x.num}, {pc.y.num})")

while pc != Point(x=None, y=None, a=a, b=b):
    pc += pp
    cc += 1
    if pc == Point(x=None, y=None, a=a, b=b):
        print(f"{cc} -- (None, None)")
    else:
        print(f"{cc} -- ({pc.x.num}, {pc.y.num})")
"""

"""
prime = 223

x = FieldElement(num=15, prime=prime)
y = FieldElement(num=86, prime=prime)
a = FieldElement(num=0, prime=prime)
b = FieldElement(num=7, prime=prime)

pp = Point(x=x, y=y, a=a, b=b)
pc = pp
res = Point(x=None, y=None, a=a, b=b)

coeff = 100_000

while coeff:

    if coeff & 1:
        res += pc

        if res == Point(x=None, y=None, a=a, b=b):
            print(f"(None, None)")
        else:
            print(f"({res.x.num}, {res.y.num})")

    pc += pc
    if pc == Point(x=None, y=None, a=a, b=b):
        print(f"* (None, None)")
    else:
        print(f"* ({pc.x.num}, {pc.y.num})")


    coeff = coeff >> 1

"""

e1 = S256_Field(num=13)
print(e1)

from src.py_bitcoin import S256_N, S256_G

print(S256_N * S256_G)