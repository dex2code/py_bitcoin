from src.py_bitcoin.fields import FieldElement

prime = 17
num1, num2 = 7, 9

fe_1 = FieldElement(num=num1, prime=prime)
fe_2 = FieldElement(num=num2, prime=prime)

print(fe_1) # FE_7_17
print(fe_2) # FE_9_17

print(fe_1 == fe_2) # False
print(fe_1 != fe_2) # True

print(fe_1 + fe_2) # FE_16_17
print(fe_1 - fe_2) # FE_15_17

print(fe_1 * fe_2) # FE_12_17
print(fe_1 / fe_2) # FE_14_17

print(fe_1**9) # FE_10_17
print(fe_1**fe_2) # FE_10_17


from src.py_bitcoin.curves import Point

# y^2 = x^3 + ax + b
a, b = 5, 7
x1, y1 = 2, 5
x2, y2 = -1, -1

point_1 = Point(x=x1, y=y1, a=a, b=b)
point_2 = Point(x=x2, y=y2, a=a, b=b)
point_3 = Point(x=None, y=None, a=a, b=b) # Infinity point on curve

print(point_1) # P_(2, 5) on 'x**3 + 5*x + 7'
print(point_2) # P_(-1, -1) on 'x**3 + 5*x + 7'
print(point_3) # P_(I) on 'x**3 + 5*x + 7'

print(point_1 == point_2) # False
print(point_1 != point_2) # True

print(point_1 + point_2) # P_(2, 5) + P_(-1, -1) = P_(3.0, -7.0) on 'x**3 + 5*x + 7'
print(point_1 + point_3) # P_(2, 5) + P_(I) = P_(2, 5) on 'x**3 + 5*x + 7'
print(point_2 + point_2) # P_(-1, -1) + P_(-1, -1) = P_(18.0, 77.0) on 'x**3 + 5*x + 7'


prime = 223

a = FieldElement(num=0, prime=prime)
b = FieldElement(num=7, prime=prime)

x1 = FieldElement(num=170, prime=prime)
y1 = FieldElement(num=142, prime=prime)
point_1 = Point(x=x1, y=y1, a=a, b=b)

x2 = FieldElement(num=60, prime=prime)
y2 = FieldElement(num=139, prime=prime)
point_2 = Point(x=x2, y=y2, a=a, b=b)

print(point_1) # P_(FE_170_223, FE_142_223) on 'x**3 + FE_0_223*x + FE_7_223'
print(point_2) # P_(FE_60_223, FE_139_223) on 'x**3 + FE_0_223*x + FE_7_223'

print(point_1 == point_2) # False
print(point_1 != point_2) # True

print(point_1 + point_2) # P_(FE_220_223, FE_181_223) on 'x**3 + FE_0_223*x + FE_7_223'

print(3 * point_1) # P_(FE_31_223, FE_94_223) on 'x**3 + FE_0_223*x + FE_7_223'


# secp256k1
from src.py_bitcoin.fields import S256_FieldElement
from src.py_bitcoin.curves import S256_Point

x = S256_FieldElement(num=0x887387e452b8eacc4acfde10d9aaf7f6d9a0f975aabb10d006e4da568744d06c)
y = S256_FieldElement(num=0x61de6d95231cd89026e286df3b6ae4a894a3378e393e93a0f45b666329a0ae34)

point = S256_Point(x=x, y=y)
print(point) # S256_P_(S256_FE_0x887387e452b8eacc4acfde10d9aaf7f6d9a0f975aabb10d006e4da568744d06c, S256_FE_0x61de6d95231cd89026e286df3b6ae4a894a3378e393e93a0f45b666329a0ae34)


# ECDSA
from src.py_bitcoin.skeeper import NewKeys, Secretary
from src.py_bitcoin.u_tools import get_hash256

my_keys = NewKeys() # Generate _random_ secret and public keys
print("0x"+"{:x}".format(my_keys.private_key).zfill(64)) # 0x73bd65f5dece82838c02aed103aa05bbc174bb46cc3ae42632da60740c15aa1f
print(my_keys.public_key) # S256_P_(S256_FE_0x79404d7138fb5c37dd3b527ac15933863ce15f520b8c4c8ac8f26b6e3c4860e7, S256_FE_0x5c1a296cc2bbb50fa4b74d859677e9720bde35ed2ba1a5c99465b16706cc5c4b)

my_keys = NewKeys(secret="My strongest secret ever!") # Or you can generate predefined keys
print("0x"+"{:x}".format(my_keys.private_key).zfill(64)) # 0x000000000000004d79207374726f6e6765737420736563726574206576657221
print(my_keys.public_key) # S256_P_(S256_FE_0xf8bb54eea41bd705fdbde54d6f35d77f255783515887b252533a4db47d372b12, S256_FE_0x62668035ad55d1245a599e32937cb4661997dcb849ee76d82924bbcac512443a)

my_message = """
Commerce on the Internet has come to rely almost exclusively on financial institutions serving as
trusted third parties to process electronic payments. While the system works well enough for
most transactions, it still suffers from the inherent weaknesses of the trust based model.
Completely non-reversible transactions are not really possible, since financial institutions cannot
avoid mediating disputes. The cost of mediation increases transaction costs, limiting the
minimum practical transaction size and cutting off the possibility for small casual transactions,
and there is a broader cost in the loss of ability to make non-reversible payments for non-
reversible services. With the possibility of reversal, the need for trust spreads. Merchants must
be wary of their customers, hassling them for more information than they would otherwise need.
A certain percentage of fraud is accepted as unavoidable. These costs and payment uncertainties
can be avoided in person by using physical currency, but no mechanism exists to make payments
over a communications channel without a trusted party."""

my_message_hash = get_hash256(message=my_message)
print("0x"+"{:x}".format(my_message_hash)) # 0xf6b01c555c5d747f85f4c5fddb1335c1ad6f26c3d6ce718ca6beb378ad3f2a53

my_signature = Secretary.sign(private_key=my_keys.private_key, message_hash=my_message_hash)
print(my_signature)
"""
{
    "r": {
        "decimal": 111378587077336523312484569346926676683637853051377130327108650929846234620843,
        "hexadecimal": "0xf63e0bda6bdb172a76a6493d892f19c579963760b1d584b0dfbaa7733913a3ab"
    },
    "s": {
        "decimal": 55975739244383239987715022196599587682947219222477374139025366496787874823573,
        "hexadecimal": "0x7bc1254af206c640f82a5a2f8f0f21d8155ec2d5243779ae50c2cd653c3dbd95"
    }
}
"""

print(Secretary.verify(signature=my_signature, public_key=my_keys.public_key, message_hash=my_message_hash)) # True
print(Secretary.verify(signature=my_signature, public_key=my_keys.public_key, message_hash=my_message_hash + 1)) # False
