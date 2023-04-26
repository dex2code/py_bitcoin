import os
import sys

parent = os.path.abspath('.')
sys.path.insert(1, parent)

from io import BytesIO

from src.py_bitcoin import *
from src.py_bitcoin.curves import *
from src.py_bitcoin.fields import *
from src.py_bitcoin.skeeper import *
from src.py_bitcoin.transactions import *
from src.py_bitcoin.u_tools import *
from src.py_bitcoin.op import *

"""
tx = "0100000001032e38e9c0a84c6046d687d10556dcacc41d275ec55fc00779ac88fdf357a187000000008c493046022100c352d3dd993a981beba4a63ad15c209275ca9470abfcd57da93b58e4eb5dce82022100840792bc1f456062819f15d33ee7055cf7b5ee1af1ebcc6028d9cdb1c3af7748014104f46db5e9d61a9dc27b8d64ad23e7383a4e6ca164593c2527c038c0857eb67ee8e825dca65046b82c9331586c82e0fd1f633f25f87c161bc6f8a630121df2b3d3ffffffff0200e32321000000001976a914c398efa9c392ba6013c5e04ee729755ef7f58b3288ac000fe208010000001976a914948c765a6914d43f2a7ac177da2c2f6b52de3d7c88ac00000000"

stream = BytesIO(bytes.fromhex(tx))

my_tx = Tx.parse(stream=stream)

print(my_tx)
"""

tx_id = "3f4735eb3beb164150000b90fba6055bcff7a08ecba9352b7d29f404a658d2c9"

tx = Tx.fetch_from_explorer(tx_id=tx_id)
print(tx)
