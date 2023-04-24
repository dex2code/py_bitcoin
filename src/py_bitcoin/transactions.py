from io import BytesIO
from typing import BinaryIO

from requests import get as r_get

from . import *
from .script import Script
from .u_tools import *


class Tx:

    def __init__(self, version, ins, outs, locktime, testnet: bool = False):
        self.tx_version = version
        self.tx_ins = ins
        self.tx_outs = outs
        self.tx_locktime = locktime
        self.testnet = testnet
    

    def __repr__(self):
        tx_ins = ""
        tx_outs = ""

        for tx_in in self.tx_ins:
            tx_ins += tx_in.__repr__() + "\n"
        
        for tx_out in self.tx_outs:
            tx_outs += tx_out.__repr__() + "\n"
        
        return f"tx: {self.tx_id()}\n" + \
            f"version: {self.tx_version}\n" + \
            f"tx_ins({len(self.tx_ins)}):\n{tx_ins}" + \
            f"tx_outs({len(self.tx_outs)}):\n{tx_outs}" + \
            f"locktime: {self.tx_locktime}"
    

    def serialize(self):
        result = int_to_le(input_int=self.tx_version, output_length=TX_VERSION_SIZE)

        result += encode_varint(i=len(self.tx_ins))
        for tx_in in self.tx_ins:
            result += tx_in.serialize()

        result += encode_varint(i=len(self.tx_outs))
        for tx_out in self.tx_outs:
            result += tx_out.serialize()

        result += int_to_le(input_int=self.tx_locktime, output_length=TX_LOCKTIME_SIZE)

        return result


    def tx_hash(self, to_int: bool = True):
        return get_hash256(message=self.serialize()[::-1], to_int=to_int)


    def tx_id(self):
        return self.tx_hash(to_int=False).hex()
    

    @classmethod
    def parse(cls, stream: BinaryIO, testnet: bool = False):
        tx_version = le_to_int(input_bytes=stream.read(TX_VERSION_SIZE))

        inputs = []
        num_inputs = read_varint(stream=stream)
        for _ in range(num_inputs):
            inputs.append(TxIn.parse(stream=stream))
        
        outputs = []
        num_outputs = read_varint(stream=stream)
        for _ in range(num_outputs):
            outputs.append(TxOut.parse(stream=stream))
        
        locktime = le_to_int(input_bytes=stream.read(TX_LOCKTIME_SIZE))

        return cls(tx_version, inputs, outputs, locktime, testnet=testnet)
    

    @classmethod
    def fetch_from_explorer(cls, tx_id: str, explorer_url: str = TX_EXPLORER_URL, testnet: bool = False):
        explorer_url = explorer_url.replace("%tx_id%", tx_id, 1)

        try:
            get_r = r_get(url=explorer_url, timeout=10)
            get_r.close()
        except Exception as E:
            raise RuntimeError("TX explorer isn't available. Try later.")
        
        if get_r.status_code != 200:
            raise RuntimeError(f"TX explorer returned an error (error='{get_r.status_code}'). Try later.")
        
        try:
            tx_raw = bytes.fromhex(get_r.text.strip())
        except Exception as E:
            raise ValueError(f"Unexpected response from explorer: '{get_r.text}'")
        
        try:
            tx = Tx.parse(stream=BytesIO(tx_raw), testnet=testnet)
        except Exception as E:
            raise ValueError(f"Cannot parse TX obtained from explorer.")
        
        return cls(tx.tx_version, tx.tx_ins, tx.tx_outs, tx.tx_locktime, tx.testnet)


class TxIn:
    
    def __init__(self, prev_tx, prev_index, script_sig=None, sequence=0xffffffff):
        self.prev_tx = prev_tx
        self.prev_index = prev_index

        if script_sig is None:
            self.script_sig = Script()
        else:
            self.script_sig = script_sig
        
        self.sequence = sequence


    def __repr__(self):
        return f"{self.prev_tx.hex()}:{self.prev_index}"
    

    @classmethod
    def parse(cls, stream: BinaryIO, testnet: bool = False):
        prev_tx = stream.read(TX_INPUT_PREV_TX_SIZE)[::-1]
        prev_index = le_to_int(input_bytes=stream.read(TX_INPUT_PREV_INDEX_SIZE))
        script_sig = Script.parse(stream=stream)
        sequence = le_to_int(input_bytes=stream.read(TX_INPUT_SEQUENCE_SIZE))

        return cls(prev_tx, prev_index, script_sig, sequence)


    def serialize(self):
        result = self.prev_tx[::-1]
        result += int_to_le(input_int=self.prev_index, output_length=TX_INPUT_PREV_INDEX_SIZE)
        #result += self.script_sig.serialize()
        result += int_to_le(input_int=self.sequence, output_length=TX_INPUT_SEQUENCE_SIZE)

        return result


class TxOut:
    
    def __init__(self, amount, script_pubkey):
        self.amount = amount
        self.script_pubkey = script_pubkey
    

    def __repr__(self):
        return f"{self.amount}:{self.script_pubkey}"
    

    @classmethod
    def parse(cls, stream: BinaryIO):
        amount = le_to_int(input_bytes=stream.read(TX_OUTPUT_AMOUNT_SIZE))
        script_pubkey = Script.parse(stream=stream)

        return cls(amount, script_pubkey)
    

    def serialize(self):
        result = int_to_le(input_int=self.amount, output_length=TX_OUTPUT_AMOUNT_SIZE)
        #result += self.script_pubkey.serialize()

        return result


if __name__ == "__main__":
    pass