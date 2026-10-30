import hashlib, time, json, os

class Block:
    def __init__(self, index, prev_hash, data, nonce=0):
        self.index = index
        self.prev_hash = prev_hash
        self.timestamp = time.time()
        self.data = data
        self.nonce = nonce
        self.hash = self.calc_hash()
    
    def calc_hash(self):
        txt = f"{self.index}{self.prev_hash}{self.timestamp}{self.data}{self.nonce}"
        return hashlib.sha256(txt.encode()).hexdigest()

class B_Coin:
    def __init__(self):
        self.file = "blockchain.json"
        if os.path.exists(self.file):
            with open(self.file) as f:
                chain_data = json.load(f)
                self.chain = []
                for b in chain_data:
                    block = Block(b['index'], b['prev_hash'], b['data'], b['nonce'])
                    block.timestamp = b['timestamp']
                    block.hash = b['hash']
                    self.chain.append(block)
        else:
            self.chain = [self.genesis()]
            self.save()
    
    def genesis(self):
        block = Block(0, "0"*64, {"msg": "B-Coin Genesis - Kalapagenep 29 Okt 2026 - by wtanta84"}, 0)
        # Mining genesis
        while not block.hash.startswith("0000"):
            block.nonce += 1
            block.hash = block.calc_hash()
        print(f"Genesis Hash: {block.hash}")
        return block
    
    def save(self):
        data = []
        for b in self.chain:
            data.append({"index": b.index, "prev_hash": b.prev_hash, "timestamp": b.timestamp, "data": b.data, "nonce": b.nonce, "hash": b.hash})
        with open(self.file, "w") as f:
            json.dump(data, f, indent=2)
    
    def add_block(self, data):
        prev = self.chain[-1]
        block = Block(len(self.chain), prev.hash, data)
        while not block.hash.startswith("0000"):
            block.nonce += 1
            block.hash = block.calc_hash()
        self.chain.append(block)
        self.save()
        print(f"Block {block.index} mined: {block.hash[:50]}...")
        print(f"Total Supply: {len(self.chain)*50} B-Coin")
        return block
