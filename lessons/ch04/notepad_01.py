import os, sys

parent = os.path.abspath('.')
sys.path.insert(1, parent)

from src.py_bitcoin import S256_Gx, S256_Gy, S256_N
from src.py_bitcoin.u_tools import get_hash256, get_random_secret, get_deterministic_k
from src.py_bitcoin.fields import S256_FieldElement
from src.py_bitcoin.curves import S256_Point
from src.py_bitcoin.skeeper import Wallet, Signature
import json
from src.py_bitcoin.skeeper import Secretary


my_wallet = Wallet(secret=0x12345deadbeef)
print(my_wallet.address(compressed=True, testnet=False))
