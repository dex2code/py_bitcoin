from src.py_bitcoin.fields import FieldElement

prime = 17

num_1 = 7
num_2 = 9

fe_1 = FieldElement(num=num_1, prime=prime)
fe_2 = FieldElement(num=num_2, prime=prime)

print(fe_1) # FE_'7'_'17'
print(fe_2) # FE_'9'_'17'

print(fe_1 == fe_2) # False
print(fe_1 != fe_2) # True

print(fe_1 + fe_2) # FE_'16'_'17'
print(fe_1 - fe_2) # FE_'15'_'17'

print(fe_1 * fe_2) # FE_'12'_'17'
print(fe_1 / fe_2) # FE_'14'_'17'

print(fe_1**9) # FE_'10'_'17'
print(fe_1**fe_2) # FE_'10'_'17'


from src.py_bitcoin.curves import Point

