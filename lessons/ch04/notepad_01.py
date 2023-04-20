import os, sys

parent = os.path.abspath('.')
sys.path.insert(1, parent)

from src.py_bitcoin import S256_Gx, S256_Gy, S256_N
from src.py_bitcoin.u_tools import get_hash256, get_random_secret, get_deterministic_k
from src.py_bitcoin.fields import S256_FieldElement
from src.py_bitcoin.curves import S256_Point
from src.py_bitcoin.skeeper import GenerateKeys, Signature
import json
from src.py_bitcoin.skeeper import Secretary


sig = Signature(r=0x37206a0610995c58074999cb9767b87af4c4978db68c06e8e6e81d282047a7c6, s=0x8ca63759c1157ebeaec0d03cecca119fc9a75bf8e6d0fa65c841c8e2738cdaec)
print(sig)
print(sig.der_value().hex())