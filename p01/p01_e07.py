from base import FieldElement


prime = [7, 11, 17, 31]

for p in prime:

    print("[", end=" ")

    for n in range(1, p):
        nn = FieldElement(n, p)

        res_nn = nn ** (p - 1)
        print(res_nn.num, end=" ")
    
    print("]")
print()


"""
n**(p-1) % p = 1 !!! 
"""

n = 128
p = 67 # ПРОСТОЕ!
print( (n ** (p - 1)) % p )