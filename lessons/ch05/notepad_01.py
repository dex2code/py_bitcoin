import os, sys

parent = os.path.abspath('.')
sys.path.insert(1, parent)

from src.py_bitcoin import *
from src.py_bitcoin.u_tools import *
from src.py_bitcoin.fields import *
from src.py_bitcoin.curves import *
from src.py_bitcoin.skeeper import *
from src.py_bitcoin.transactions import *


my_tx = Tx(version=1, ins=[1, 2], outs=[3, 4], locktime=0, testnet=False)

print(my_tx)
print()

print(my_tx.tx_id())
print()
