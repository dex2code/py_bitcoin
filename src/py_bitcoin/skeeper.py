from .u_tools import get_random_secret, get_hash256, get_deterministic_k
from .curves import S256_Point
from . import S256_N, S256_Gx, S256_Gy, S256_A, S256_B
from json import dumps as json_dumps

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

        mod_secret = secret_ % S256_N
        if mod_secret == 0:
            raise ValueError("Your secret is equal to S256_N number. Try another one.")
        
        self.private_key = mod_secret
        self.public_key = (secret_ * S256_Point(x=S256_Gx, y=S256_Gy)).x.num
    

    def __repr__(self) -> str:
        my_repr = {
            "private_key": {
                "decimal": self.private_key,
                "hexadecimal": "0x"+"{:x}".format(self.private_key).zfill(64)
            },
            "public_key": {
                "decimal": self.public_key,
                "hexadecimal": "0x"+"{:x}".format(self.public_key).zfill(64)
            }
        }

        return json_dumps(obj=my_repr, indent=4)


class Signature:

    def __init__(self, rx, ry, s):
        self.rx = rx
        self.ry = ry
        self.s = s


    def __repr__(self) -> str:
        my_repr = {
            "rx": {
                "decimal": self.rx,
                "hexadecimal": "0x"+"{:x}".format(self.rx).zfill(64)
            },
            "ry": {
                "decimal": self.ry,
                "hexadecimal": "0x"+"{:x}".format(self.ry).zfill(64)
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
        rx = p.x.num
        ry = p.y.num
        s = (message_hash + rx * private_key) * k_inv % S256_N

        if s > (S256_N / 2):
            s = S256_N - s
        
        return Signature(rx=rx, ry=ry, s=s), p


    def verify(signature: Signature, message_hash: int) -> bool:
        S256_G = S256_Point(x=S256_Gx, y=S256_Gy)
        s_inv = pow(signature.s, S256_N - 2, S256_N)
        
        u = message_hash * s_inv % S256_N
        v = signature.rx * s_inv % S256_N
        
        total = (u * S256_G) + (v * S256_Point(x=signature.rx, y=signature.ry))

        return total.x.num == signature.rx

        