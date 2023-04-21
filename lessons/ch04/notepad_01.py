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


my_wallet = Wallet(secret="KxU4tne85nJo7oDRNcATqvdyiDUY8gfRNiTQPQyyey3RkQu3mZxp")
wif_key = my_wallet.private_key.wif_value()
btc_address = my_wallet.address()
print(f"{wif_key=}")
print(f"{btc_address=}")
print()
