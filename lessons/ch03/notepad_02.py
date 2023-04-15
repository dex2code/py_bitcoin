import os, sys, time

parent = os.path.abspath('.')
sys.path.insert(1, parent)

from src.py_bitcoin import S256_Gx, S256_Gy, S256_N
from src.py_bitcoin.u_tools import get_hash256, get_random_secret, get_deterministic_k
from src.py_bitcoin.curves import S256_Point
from src.py_bitcoin.skeeper import NewKeys
import json
from src.py_bitcoin.skeeper import Secretary


my_keys = NewKeys(secret=12345)
print(f"Private key: {my_keys.private_key}")
print(f"Public key: {my_keys.public_key}")

my_message = "Programming Bitcoin!"
my_message_hash = get_hash256(my_message)
print(f"Message hash: {my_message_hash}")
print(f"Message hash: {hex(my_message_hash)}")

my_signature, p = Secretary.sign(private_key=my_keys.private_key, message_hash=my_message_hash)
print(my_signature)
print(p)

bb = Secretary.verify(signature=my_signature, message_hash=my_message_hash)
print(bb) 