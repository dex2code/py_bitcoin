"""
Finite Fields
"""
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


"""
Elliptic Curves
"""
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
print(point)
"""
{
    "x": {
        "int": 61718672711110078285455301750480400966627255360668707636501858927943098880108,
        "hex": "0x887387e452b8eacc4acfde10d9aaf7f6d9a0f975aabb10d006e4da568744d06c"
    },
    "y": {
        "int": 44267342672039291314052509441658516950140155852350072275186874907549665111604,
        "hex": "0x61de6d95231cd89026e286df3b6ae4a894a3378e393e93a0f45b666329a0ae34"
    }
}
"""


"""
Elliptic Curve Cryptography
"""
# ECDSA
from src.py_bitcoin.skeeper import Wallet, Secretary
from src.py_bitcoin.u_tools import get_hash256

my_wallet = Wallet() # Generate _random_ secret and public keys
print(my_wallet.private_key)
"""
{
    "int": 115777494148019931866928113890741224965578616471279673064180114706432139966072,
    "hex": "0xfff7bd4e0cd4f86d41fb642816a3c159689a2a8db3f5f06ef24b886ea077b678"
}
"""
print(my_wallet.private_key.wif_value(compressed=True, testnet=False)) # L4mWuYgF9vQc4jVqPPmGQ1ViQZuEDE514Q3VzDrnHQQTDFv1ABWy
print(my_wallet.private_key.wif_value(compressed=True, testnet=True))

print(my_wallet.public_key)
"""
{
    "x": {
        "int": 93271287992545152956520593913782910473001718494328213378720471074176997597899,
        "hex": "0xce35ad9f0b7c268354fc70a9c342dfb620f5f1d24a0fea39ed89f04d0d4d22cb"
    },
    "y": {
        "int": 99171575440654798010829414499551646342496980177395937607359861879590642669321,
        "hex": "0xdb411f5ffa775f77ce031f863520daadc5198b5dcef1745e7e58a800f3065709"
    }
}
"""
print(my_wallet.public_key.sec_value(compressed=False).hex()) # 04e68d04cbee99c26f93ace023b285ed1844ed63c8581a19879dfb25c9728c13d90864e086883af0e8fce9136c533641306ac6b172e13ce921a0b29fc67b745262
print(my_wallet.public_key.sec_value(compressed=True).hex()) # 02e68d04cbee99c26f93ace023b285ed1844ed63c8581a19879dfb25c9728c13d9
print(my_wallet.address(testnet=True)) # mj4phvNSRUB5cNoe35Dq64ozswt975u2KR
print(my_wallet.address(testnet=False)) # 165FxuZx78gnBduuQQsrYxQ3aEeYHCeiD8

my_wallet = Wallet(secret="My strongest secret ever!") # Or you can generate predefined keys
print(my_wallet.private_key)
"""
{
    "int": 486306853179768214323147254942175147312001728581351145566753,
    "hex": "0x000000000000004d79207374726f6e6765737420736563726574206576657221"
}
"""
print(my_wallet.public_key)
"""
{
    "x": {
        "int": 112504573030206727894118935474377214458828245115960272018274514385709645114130,
        "hex": "0xf8bb54eea41bd705fdbde54d6f35d77f255783515887b252533a4db47d372b12"
    },
    "y": {
        "int": 44507762432431393322097723613868253877949735835700089981781062023154114905146,
        "hex": "0x62668035ad55d1245a599e32937cb4661997dcb849ee76d82924bbcac512443a"
    }
}
"""
print(my_wallet.public_key.sec_value(compressed=False).hex()) # 04f8bb54eea41bd705fdbde54d6f35d77f255783515887b252533a4db47d372b1262668035ad55d1245a599e32937cb4661997dcb849ee76d82924bbcac512443a
print(my_wallet.public_key.sec_value(compressed=True).hex()) # 02f8bb54eea41bd705fdbde54d6f35d77f255783515887b252533a4db47d372b12
print(my_wallet.address(testnet=True)) # mjuS52MD5AH6VRzPHQFrmpvDrWAQxgyWrv
print(my_wallet.address(testnet=False)) # 15PUmyGEG8qqiKWmZqHUwuhtzWZi7P75ZJ

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

my_signature = Secretary.sign(private_key=my_wallet.private_key, message_hash=my_message_hash)
print(my_signature)
"""
{
    "r": {
        "int": 111378587077336523312484569346926676683637853051377130327108650929846234620843,
        "hex": "0xf63e0bda6bdb172a76a6493d892f19c579963760b1d584b0dfbaa7733913a3ab"
    },
    "s": {
        "int": 55975739244383239987715022196599587682947219222477374139025366496787874823573,
        "hex": "0x7bc1254af206c640f82a5a2f8f0f21d8155ec2d5243779ae50c2cd653c3dbd95"
    }
}
"""
print(my_signature.der_value().hex())
"""
3045022100f63e0bda6bdb172a76a6493d892f19c579963760b1d584b0dfbaa7733913a3ab02207bc1254af206c640f82a5a2f8f0f21d8155ec2d5243779ae50c2cd653c3dbd95
"""

print(Secretary.verify(signature=my_signature, public_key=my_wallet.public_key, message_hash=my_message_hash)) # True
print(Secretary.verify(signature=my_signature, public_key=my_wallet.public_key, message_hash=my_message_hash + 1)) # False
