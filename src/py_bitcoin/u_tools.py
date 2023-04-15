from . import S256_N
from hashlib import sha256
import hmac
from requests import get as r_get


def get_hash256(__value: any) -> int:
    """
    This function takes an arbitrary text or byte string as an argument
    and returns a double hash of that argument as a byte string.
    """
    if type(__value) == str:
        input_text = __value.encode(encoding="utf-8")
    elif type(__value) == bytes:
        input_text = __value
    else:
        raise TypeError("Input object should be <str> or <bytes>")
    
    first_hash = sha256(input_text).digest()
    second_hash = sha256(first_hash).digest()
    final_hash = int.from_bytes(bytes=second_hash, byteorder="big")

    return final_hash


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
        raise RuntimeError("Cannot get random K. Try later.")
    
    if get_r.status_code != 200:
        raise RuntimeError("Cannot get random K. Try later.")
    
    random_secret = ''.join(get_r.text.split())
    if len(random_secret) != 2 * 32:
        raise ValueError("Obtained random secret is defective. Try again.")
    
    try:
        random_secret = int(random_secret, base=16)
        random_secret = random_secret % S256_N
        if random_secret == 0:
            random_secret = random_secret + 1
    except Exception as E:
        raise ValueError("Obtained random secret is defective. Try again.")
    
    return random_secret


def get_deterministic_k(private_key: int, message_hash: int) -> int:
    """
    This function returns a deterministic value of 'k' relative to your private key and message hash.
    """
    k = b'\x00' * 32
    v = b'\x01' * 32

    if message_hash > S256_N:
        message_hash = message_hash - S256_N

    message_hash_bytes = message_hash.to_bytes(length=32, byteorder="big")
    private_key_bytes = private_key.to_bytes(length=32, byteorder="big")

    s256 = sha256

    k = hmac.new(k, v + b'\x00' + private_key_bytes + message_hash_bytes, s256).digest()
    v = hmac.new(k, v, s256).digest()
    k = hmac.new(k, v + b'\x01' + private_key_bytes + message_hash_bytes, s256).digest()
    v = hmac.new(k, v, s256).digest()
    
    while True:
        v = hmac.new(k, v, s256).digest()
        candidate_k = int.from_bytes(bytes=v, byteorder="big")
        if candidate_k >= 1 and candidate_k < S256_N:
            return candidate_k
        k = hmac.new(k, v + b'\x00', s256).digest()
        v = hmac.new(k, v, s256).digest()


if __name__ == "__main__":
    pass