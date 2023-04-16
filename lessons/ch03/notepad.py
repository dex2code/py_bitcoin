import os, sys

parent = os.path.abspath('.')
sys.path.insert(1, parent)


import src.py_bitcoin.u_tools as u_tools
import src.py_bitcoin.skeeper as skeeper


my_message = "Programming Bitcoin!"
my_message_hash = u_tools.get_hash256(message=my_message)

my_keys = skeeper.NewKeys(secret="My_Secret")

my_signature = skeeper.Secretary.sign(private_key=my_keys.private_key, message_hash=my_message_hash)

bb = skeeper.Secretary.verify(signature=my_signature, public_key=my_keys.public_key, message_hash=my_message_hash)

print(bb)