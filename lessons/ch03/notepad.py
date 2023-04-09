import os, sys

parent = os.path.abspath('.')
sys.path.insert(1, parent)


from src.py_bitcoin.curves import Point
from src.py_bitcoin.fields import FieldElement


print(FieldElement(7, 11))


