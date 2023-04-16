import os, sys

parent = os.path.abspath('.')
sys.path.insert(1, parent)

from src.py_bitcoin import S256_Gx, S256_Gy, S256_N
from src.py_bitcoin.u_tools import get_hash256, get_random_secret, get_deterministic_k
from src.py_bitcoin.fields import S256_FieldElement
from src.py_bitcoin.curves import S256_Point
from src.py_bitcoin.skeeper import NewKeys
import json
from src.py_bitcoin.skeeper import Secretary

x = S256_FieldElement(num=0x887387e452b8eacc4acfde10d9aaf7f6d9a0f975aabb10d006e4da568744d06c)
y = S256_FieldElement(num=0x61de6d95231cd89026e286df3b6ae4a894a3378e393e93a0f45b666329a0ae34)

p = S256_Point(x=x, y=y)

print(p)