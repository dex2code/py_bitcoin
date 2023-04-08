from base import FieldElement


k = [1, 3, 7, 13, 18]
prime = 19


for kk in k:
    kkk = FieldElement(kk, prime)

    print("[", end=" ")

    for i in range(prime):
        ii = FieldElement(i, prime)

        k_res = kkk * ii

        print(k_res.num, end=" ")
    
    print("]")
