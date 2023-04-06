from base import FieldElement


prime = 57


a = 44
b = 33
print( (a + b) % prime )
aa = FieldElement(a, prime)
bb = FieldElement(b, prime)
print(aa + bb)
print()


a = 9
b = 29
print( (a - b) % prime )
aa = FieldElement(a, prime)
bb = FieldElement(b, prime)
print(aa - bb)
print()


a = 17
b = 42
c = 49
print( (a + b + c) % prime )
aa = FieldElement(a, prime)
bb = FieldElement(b, prime)
cc = FieldElement(c, prime)
print(aa + bb + cc)
print()


a = 52
b = 30
c = 38
print( (a - b - c) % prime )
aa = FieldElement(a, prime)
bb = FieldElement(b, prime)
cc = FieldElement(c, prime)
print(aa - bb - cc)
print()
