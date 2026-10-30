import json, hashlib, os, time, random

WALLETS_FILE = "wallets.json"

def create_wallet(name):
    # Simple wallet generation
    private_key = hashlib.sha256(f"{name}{time.time()}{random.random()}".encode()).hexdigest()
    address = "BCOIN_" + hashlib.sha256(private_key.encode()).hexdigest()[:16].upper()
    
    wallets = {}
    if os.path.exists(WALLETS_FILE):
        wallets = json.load(open(WALLETS_FILE))
    
    if name in wallets:
        print(f"⚠️ Wallet '{name}' already exists!")
        print(f"   Address: {wallets[name]['address']}")
        return wallets[name]
    
    wallets[name] = {
        "address": address,
        "private_key": private_key,
        "created": int(time.time()*1000)
    }
    json.dump(wallets, open(WALLETS_FILE,'w'), indent=2)
    print(f"✅ Wallet Created!")
    print(f"   Name: {name}")
    print(f"   Address: {address}")
    print(f"   Private Key: {private_key[:12]}... (KEEP SECRET!)")
    return wallets[name]

def list_wallets():
    if not os.path.exists(WALLETS_FILE):
        print("No wallets yet. Create with: python3 wallet.py create <name>")
        return
    wallets = json.load(open(WALLETS_FILE))
    chain = json.load(open('blockchain.json'))
    # Calculate balances
    balances = {}
    for block in chain:
        d = block['data']
        if 'to' in d:
            balances[d['to']] = balances.get(d['to'], 0) + d['amount']
        if 'from' in d and not d['from'].startswith('miner_') and d['from'] != 'genesis':
            balances[d['from']] = balances.get(d['from'], 0) - d['amount']
    
    print(f"\n💼 Wallets ({len(wallets)}):")
    for name, w in wallets.items():
        bal = balances.get(w['address'], balances.get(name, 0))
        print(f"   {name}: {w['address']} | Balance: {bal} BCOIN")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 wallet.py create wtanta84")
        print("  python3 wallet.py create budi")
        print("  python3 wallet.py list")
    elif sys.argv[1] == "create" and len(sys.argv) > 2:
        create_wallet(sys.argv[2])
    elif sys.argv[1] == "list":
        list_wallets()
