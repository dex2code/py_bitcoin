from base import FieldElement

"""
a / b = ( a * b**(-1) ) % prime

b**-1 = b**(prime-2) !!!

!!! a / b = ( a * b**(prime-2) ) % prime !!!
"""

prime = 31


a = 3
b = 24
print( ( a * b**(prime-2) ) % prime )
aa = FieldElement(a, prime)
bb = FieldElement(b, prime)
print(aa / bb)
print()


"""
a ** -1 == a ** (p - 2)
a ** -2 == a ** (p - 3) => a ** -x == a ** (p - 1 - 1)
"""

a = 17
ae = -3
ae = ae % (prime - 1) #!!!!!!!!
print( (a ** ae) % prime )
aa = FieldElement(a, prime=prime)
print(aa**ae)
print()


a = 4
ae = -4
aee = ae % (prime - 1)
b = 11
print((a**aee * b) % prime)
aa = FieldElement(a, prime)
bb = FieldElement(b, prime)
print(aa**ae * bb)