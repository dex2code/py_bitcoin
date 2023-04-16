import os, sys, hashlib

parent = os.path.abspath('.')
sys.path.insert(1, parent)

from src.py_bitcoin import S256_Gx, S256_Gy, S256_N
from src.py_bitcoin.u_tools import get_hash256, get_random_secret, get_deterministic_k
from src.py_bitcoin.curves import S256_Point
from src.py_bitcoin.skeeper import NewKeys
import json
from src.py_bitcoin.skeeper import Secretary


S256_G = S256_Point(x=S256_Gx, y=S256_Gy)

e = 12345
z = get_hash256("Programming Bitcoin!")
k = get_deterministic_k(private_key=e, message_hash=z)
k_inv = pow(k, S256_N - 2, S256_N)
r = (k * S256_G).x.num
s = (z + r * e) * k_inv % S256_N


my_keys = NewKeys(secret=e)

print("Private keys equal:", e == my_keys.private_key)


my_signature, p = Secretary.sign(private_key=my_keys.private_key, message_hash=z)

print("R equal:", r == my_signature.rx)
print("S equal:", s == my_signature.s)
