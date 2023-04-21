from json import dumps as json_dumps

from . import S256_N, S256_Gx, S256_Gy
from .curves import S256_Point
from .u_tools import get_deterministic_k, get_hash256, get_random_secret


class PrivateKey:

    def __init__(self, private_key: int) -> None:
        self.int_value = private_key
        self.hex_value = "0x" +"{:x}".format(self.int_value).zfill(64)
    

    def __repr__(self) -> str:
        my_repr = {
            "int": self.int_value,
            "hex": self.hex_value
        }

        return json_dumps(obj=my_repr, indent=4)


class Signature:

    def __init__(self, r, s):
        self.r = r
        self.s = s


    def __repr__(self) -> str:
        my_repr = {
            "r": {
                "int": self.r,
                "hex": "0x"+"{:x}".format(self.r).zfill(64)
            },
            "s": {
                "int": self.s,
                "hex": "0x"+"{:x}".format(self.s).zfill(64)
            }
        }

        return json_dumps(obj=my_repr, indent=4)
    

    def der_value(self) -> bytes:
        """
        Returns DER format of Signature object
        """
        r_bin = self.r.to_bytes(length=32, byteorder="big").lstrip(b'\x00')
        
        if r_bin[0] & 0x80:
            r_bin = b'\x00' + r_bin
        
        result = bytes([2, len(r_bin)]) + r_bin

        s_bin = self.s.to_bytes(length=32, byteorder="big").lstrip(b'\x00')

        if s_bin[0] & 0x80:
            s_bin = b'\x00' + s_bin

        result = result + bytes([2, len(s_bin)]) + s_bin
        
        result = bytes([0x30, len(result)]) + result

        return result

class Wallet:

    def __init__(self, secret=get_random_secret()):
        if type(secret) == int:
            secret_ = secret
        elif type(secret) == bytes:
            secret_ = int.from_bytes(bytes=secret, byteorder="big")
        elif type(secret) == str:
            secret_ = int.from_bytes(bytes=secret.encode(encoding="utf-8"), byteorder="big")
        else:
            raise TypeError("Given secret must have type <int>, <str> or <bytes>")

        if secret_ > S256_N:
            secret_ = secret_ % S256_N
        
        if secret_ == 0:
            raise ValueError("Your secret calculated to zero number. Try another one.")
        
        S256_G = S256_Point(x=S256_Gx, y=S256_Gy)

        self.private_key = PrivateKey(private_key=secret_)
        self.public_key = secret_ * S256_G
        
    
    def address(self, compressed=True, testnet=False):
        return self.public_key.address_value(compressed=compressed, testnet=testnet).decode()


class Secretary:

    def sign(private_key: PrivateKey, message_hash: int) -> Signature:
        if type(private_key) != PrivateKey or type(message_hash) != int:
            raise TypeError("(Secretary.sign) Wrong attributes type!")

        k = get_deterministic_k(private_key=private_key.int_value, message_hash=message_hash)
        k_inv = pow(k, S256_N - 2, S256_N)

        S256_G = S256_Point(x=S256_Gx, y=S256_Gy)

        p = k * S256_G
        r = p.x.num
        s = (message_hash + r * private_key.int_value) * k_inv % S256_N

        if s > (S256_N / 2):
            s = S256_N - s
        
        return Signature(r=r, s=s)


    def verify(signature: Signature, public_key: S256_Point, message_hash: int) -> bool:
        s_inv = pow(signature.s, S256_N - 2, S256_N)
        
        u = message_hash * s_inv % S256_N
        v = signature.r * s_inv % S256_N

        S256_G = S256_Point(x=S256_Gx, y=S256_Gy)
        
        total = (u * S256_G) + (v * public_key)

        return total.x.num == signature.r

        