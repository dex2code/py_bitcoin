from base import FieldElement


prime = 97


a = 95
b = 45
c = 31
print( (a * b * c) % prime)
aa = FieldElement(a, prime)
bb = FieldElement(b, prime)
cc = FieldElement(c, prime)
print(aa * bb * cc)
print()


a = 17
b = 13
c = 19
d = 44
print( (a * b * c * d) % prime)
aa = FieldElement(a, prime)
bb = FieldElement(b, prime)
cc = FieldElement(c, prime)
dd = FieldElement(d, prime)
print(aa * bb * cc * dd)
print()


a = 12
ae = 7
b = 77
be = 49
print( (a**ae * b**be) % prime)
aa = FieldElement(a, prime)
bb = FieldElement(b, prime)
print(aa**ae * bb**be)
print()
