import hashlib, time, json, random
def create_wallet(username="wtanta84"):
    private_key = hashlib.sha256(f"{username}{time.time()}{random.random()}".encode()).hexdigest()
    public_key = hashlib.sha256(private_key.encode()).hexdigest()
    address = f"B{hashlib.sha256(public_key.encode()).hexdigest()[:34]}"
    wallet = {"username": username, "address": address, "private_key": private_key, "public_key": public_key, "balance": 0, "created": "2026-10-29 Kalapagenep"}
    with open(f"{username}_wallet.json", "w") as f: json.dump(wallet, f, indent=2)
    print("=== B-Coin Wallet Created ===")
    print(f"User: {username}")
    print(f"Address: {address}")
    print("File saved!")
    return wallet
create_wallet("wtanta84")
