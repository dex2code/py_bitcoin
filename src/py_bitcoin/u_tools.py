import hmac
from hashlib import sha256
from typing import Union

from requests import get as r_get

from . import S256_N

import base58


def be_to_int(input_bytes: bytes) -> int:
    if type(input_bytes) != bytes:
        raise TypeError("(u_tools.be_to_int) Input data is not bytes.")
    
    return int.from_bytes(bytes=input_bytes, byteorder="big")


def le_to_int(input_bytes: bytes) -> int:
    if type(input_bytes) != bytes:
        raise TypeError("(u_tools.le_to_int) Input data is not bytes.")
    
    return int.from_bytes(bytes=input_bytes, byteorder="little")


def int_to_be(input_int: int, output_length: int = 32) -> bytes:
    if type(input_int) != int or type(output_length) != int:
        raise TypeError("(u_tools.int_to_be) Input data is not int.")

    return input_int.to_bytes(length=output_length, byteorder="big")


def int_to_le(input_int: int, output_length: int = 32) -> bytes:
    if type(input_int) != int or type(output_length) != int:
        raise TypeError("(u_tools.int_to_le) Input data is not int.")

    return input_int.to_bytes(length=output_length, byteorder="little")


def get_hash256(message: Union[str, bytes], to_int=True) -> Union[int, bytes]:
    """
    This function takes an arbitrary text or byte string as an argument
    and returns a double hash SHA256 of that argument as a int number.
    """
    if type(message) == str:
        input_text = message.encode(encoding="utf-8")
    elif type(message) == bytes:
        input_text = message
    else:
        raise TypeError("(u_tools.get_hash256) Input object should be <str> or <bytes>!")
    
    first_hash = sha256(input_text).digest()
    second_hash = sha256(first_hash).digest()

    if to_int:
        final_hash = be_to_int(input_bytes=second_hash)
        return final_hash
    else:
        return second_hash


def get_random_secret() -> int:
    """
    This function returns a completely random number between 0 and (S256_N - 1).
    If the random value generator is not available or returned an error, the function will also return a RuntimeError.
    """
    random_api = "https://www.random.org/integers/?num=32&min=0&max=255&col=32&base=16&format=plain&rnd=new"

    try:
        get_r = r_get(url=random_api, timeout=5)
        get_r.close()
    except Exception as E:
        raise RuntimeError("(u_tools.get_random_secret) Cannot get random secret. Try later.")
    
    if get_r.status_code != 200:
        raise RuntimeError("(u_tools.get_random_secret) Cannot get random secret. Try later.")
    
    random_secret = ''.join(get_r.text.split())
    if len(random_secret) != 2 * 32:
        raise ValueError(f"(u_tools.get_random_secret) Obtained random secret is defective ('{random_secret}'). Try again.")
    
    try:
        random_secret = int(random_secret, base=16)
        if random_secret > S256_N:
            random_secret = random_secret - S256_N
    except Exception as E:
        raise ValueError(f"(u_tools.get_random_secret) Obtained random secret is defective ('{random_secret}'). Try again.")
    
    return random_secret


def get_deterministic_k(private_key: int, message_hash: int) -> int:
    """
    This function returns a deterministic value of 'k' relative to your private key and message hash.
    """
    k = b'\x00' * 32
    v = b'\x01' * 32

    if message_hash > S256_N:
        message_hash = message_hash - S256_N

    message_hash_bytes = int_to_be(input_int=message_hash)
    private_key_bytes = int_to_be(input_int=private_key)

    s256 = sha256

    k = hmac.new(k, v + b'\x00' + private_key_bytes + message_hash_bytes, s256).digest()
    v = hmac.new(k, v, s256).digest()
    k = hmac.new(k, v + b'\x01' + private_key_bytes + message_hash_bytes, s256).digest()
    v = hmac.new(k, v, s256).digest()
    
    while True:
        v = hmac.new(k, v, s256).digest()
        candidate_k = be_to_int(input_bytes=v)

        if (candidate_k >= 1) and (candidate_k < S256_N):
            return candidate_k
        
        k = hmac.new(k, v + b'\x00', s256).digest()
        v = hmac.new(k, v, s256).digest()


def wif_to_int(wif_key: str, compressed: bool = True, testnet: bool = False) -> int:
    wif_bytes = base58.b58decode_check(v=wif_key)

    if testnet and wif_bytes[0:1] != b'\xef':
        raise ValueError(f"(u_tools.wif_to_int) First byte ({wif_bytes[0:1]}) is not '0xef' for {testnet=}")
    
    if not testnet and wif_bytes[0:1] != b'\x80':
        raise ValueError(f"(u_tools.wif_to_int) First byte ({wif_bytes[0:1]}) is not '0x80' for {testnet=}")
    
    if compressed and wif_bytes[-1:] != b'\x01':
        raise ValueError(f"(u_tools.wif_to_int) Last byte ({wif_bytes[-1:]}) is not '0x01' for {compressed=}")
    
    return be_to_int(input_bytes=wif_bytes[1:-1])


if __name__ == "__main__":
    pass
