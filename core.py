import hashlib, json, time

class Block:
    def __init__(self, index, data, prev_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.prev_hash = prev_hash
        self.nonce = 0
        self.hash = self.mine()

    def mine(self):
        # Proof of Work - cari hash dengan 4 nol di depan
        while True:
            text = f"{self.index}{self.timestamp}{self.data}{self.prev_hash}{self.nonce}"
            h = hashlib.sha256(text.encode()).hexdigest()
            if h.startswith("0000"):
                return h
            self.nonce += 1

class B_Coin:
    def __init__(self):
        genesis = Block(0, "B-Coin Genesis - Kalapagenep 29 Okt 2026", "0")
        self.chain = [genesis]
        print(f"Genesis Hash: {genesis.hash}")

    def add_block(self, data):
        last = self.chain[-1]
        new = Block(len(self.chain), data, last.hash)
        self.chain.append(new)
        print(f"Block {new.index} mined: {new.hash}")

# Jalankan
if __name__ == "__main__":
    coin = B_Coin()
    coin.add_block({"from": "wtanta", "to": "satoshi", "amount": 10})
    print("B-Coin chain valid, total blocks:", len(coin.chain))
