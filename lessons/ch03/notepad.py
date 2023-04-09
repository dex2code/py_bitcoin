from fields import FieldElement
from curves import Point

"""
prime = 221
a = FieldElement(num=0,  prime=prime)
b = FieldElement(num=7,  prime=prime)
x = FieldElement(num=47, prime=prime)
y = FieldElement(num=71, prime=prime)

p = Point(x=x, y=y, a=a, b=b)

for s in range(1, 23):
    res = s * p

    print(f"{s} * (47, 71) == ({res.x}, {res.y})")
"""


e1 = FieldElement(num=0, prime=17)

for i in range(25):
    print(i + e1)