import json, hashlib, os, secrets

class Wallet:
    def __init__(self, name="wtanta84"):
        self.file = f"{name}_wallet.json"
        if os.path.exists(self.file):
            with open(self.file) as f:
                data = json.load(f)
                self.address = data['address']
                self.private_key = data['private_key']
        else:
            self.private_key = secrets.token_hex(32)
            self.address = "B" + hashlib.sha256(self.private_key.encode()).hexdigest()[:32]
            self.save()
            print(f"=== B-Coin Wallet Created ===")
            print(f"User: {name}")
            print(f"Address: {self.address}")
            print(f"Private Key: {self.private_key[:20]}... (RAHASIA!)")
    
    def save(self):
        # Hitung balance dari blockchain.json
        balance = 0
        if os.path.exists("blockchain.json"):
            with open("blockchain.json") as f:
                chain = json.load(f)
                for block in chain:
                    if block['data'].get('to') == 'wtanta84':
                        balance += block['data'].get('amount', 0)
        
        data = {
            "address": self.address,
            "private_key": self.private_key,
            "balance": balance,
            "created": "2026-10-29 Kalapagenep"
        }
        with open(self.file, "w") as f:
            json.dump(data, f, indent=2)
        return balance
    
    def get_balance(self):
        bal = self.save()
        print(f"\n💰 Wallet: {self.address}")
        print(f"💰 Balance: {bal} B-Coin")
        print(f"📦 Blocks: 26+ mined")
        return bal

if __name__ == "__main__":
    w = Wallet()
    w.get_balance()
