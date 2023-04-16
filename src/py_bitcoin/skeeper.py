from json import dumps as json_dumps

from . import S256_A, S256_B, S256_N, S256_Gx, S256_Gy
from .curves import S256_Point
from .u_tools import get_deterministic_k, get_hash256, get_random_secret


class NewKeys:

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

        self.private_key = secret_
        self.public_key = secret_ * S256_G


class Signature:

    def __init__(self, r, s):
        self.r = r
        self.s = s


    def __repr__(self) -> str:
        my_repr = {
            "r": {
                "decimal": self.r,
                "hexadecimal": "0x"+"{:x}".format(self.r).zfill(64)
            },
            "s": {
                "decimal": self.s,
                "hexadecimal": "0x"+"{:x}".format(self.s).zfill(64)
            }
        }

        return json_dumps(obj=my_repr, indent=4)


class Secretary:

    def sign(private_key: int, message_hash: int) -> Signature:
        if type(private_key) != int or type(message_hash) != int:
            raise TypeError("Both attributes must be <int>")

        k = get_deterministic_k(private_key=private_key, message_hash=message_hash)
        k_inv = pow(k, S256_N - 2, S256_N)

        S256_G = S256_Point(x=S256_Gx, y=S256_Gy)

        p = k * S256_G
        r = p.x.num
        s = (message_hash + r * private_key) * k_inv % S256_N

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

        