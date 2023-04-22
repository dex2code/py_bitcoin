import os, sys

parent = os.path.abspath('.')
sys.path.insert(1, parent)

from src.py_bitcoin import *
from src.py_bitcoin.u_tools import *
from src.py_bitcoin.fields import *
from src.py_bitcoin.curves import *
from src.py_bitcoin.skeeper import *
import json
from src.py_bitcoin.skeeper import *


my_wallet = Wallet(secret="cTVjVSWW8pvsk26NSLs9pbedQAMWxh6hSeP9hFSwbSkYbRevnKSp", wif=True, wif_compressed=True, wif_testnet=True)
wif_key = my_wallet.private_key.wif_value(compressed=True, testnet=True)
btc_address = my_wallet.address(compressed=True, testnet=True)

pub_key = my_wallet.public_key
print(pub_key)
pub_sec = my_wallet.public_key.sec_value(compressed=True)
print(pub_sec)

sp = S256_Point.restore_from_sec(sec_bytes=pub_sec)
print(sp)