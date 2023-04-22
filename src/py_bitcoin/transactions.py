from .u_tools import get_hash256


class Tx:

    def __init__(self, version, ins, outs, locktime, testnet: bool = False):
        self.version = version
        self.ins = ins
        self.outs = outs
        self.locktime = locktime
        self.testnet = testnet
    

    def __repr__(self):
        tx_ins = ""
        tx_outs = ""

        for tx_in in self.ins:
            tx_ins += tx_in.__repr__() + "\n"
        
        for tx_out in self.outs:
            tx_outs += tx_out.__repr__() + "\n"
        
        return f"tx: {self.id()}\nversion: {self.version}\ntx_ins:\n{tx_ins}tx_outs:\n{tx_outs}locktime: {self.locktime}"
    

    def serialize(self):
        pass


    def hash(self):
        return get_hash256(self.serialize()[::-1])


    def id(self):
        return self.hash().hex()
    

    @classmethod
    def parse(cls, stream):
        pass