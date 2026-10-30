import json, time, hashlib, os, sys
from config import get_reward

def get_balance(address):
    chain = json.load(open('blockchain.json'))
    bal = 0
    for block in chain:
        d = block['data']
        if d.get('to') == address:
            bal += d['amount']
        if d.get('from') == address:
            bal -= d['amount']
    # Also check wallet name alias
    if os.path.exists("wallets.json"):
        wallets = json.load(open("wallets.json"))
        for name, w in wallets.items():
            if w['address'] == address:
                # check alias name too
                for b in chain:
                    if b['data'].get('to') == name:
                        bal += b['data']['amount']
                    if b['data'].get('from') == name:
                        bal -= b['data']['amount']
    return bal

def transfer(from_addr, to_addr, amount):
    amount = float(amount)
    chain = json.load(open('blockchain.json'))
    
    # Resolve wallet names to addresses
    if os.path.exists("wallets.json"):
        wallets = json.load(open("wallets.json"))
        if from_addr in wallets:
            from_addr = wallets[from_addr]['address']
        if to_addr in wallets:
            to_addr = wallets[to_addr]['address']
    
    # Also allow name directly as balance holder
    bal = get_balance(from_addr)
    # Try name balance if address balance 0
    if bal == 0:
        # check if from_addr is actually a name with balance like wtanta84
        temp_bal = 0
        for b in chain:
            if b['data'].get('to') == from_addr or b['data'].get('to') == from_addr.lower():
                temp_bal += b['data']['amount']
            if b['data'].get('from') == from_addr:
                temp_bal -= b['data']['amount']
        if temp_bal > 0:
            bal = temp_bal
    
    # For wtanta84 legacy
    if from_addr.startswith("BCOIN_") == False and from_addr == "wtanta84":
        bal = sum([b['data']['amount'] for b in chain if b['data'].get('to') == 'wtanta84'])

    if bal < amount:
        print(f"❌ Insufficient balance! {from_addr} has {bal} BCOIN, need {amount}")
        return False
    
    last = chain[-1]
    idx = len(chain)
    ts = int(time.time()*1000)
    data = {"from": from_addr, "to": to_addr, "amount": amount, "type": "transfer"}
    h = hashlib.sha256(f"{idx}{last['hash']}{ts}{str(data)}{idx}".encode()).hexdigest()
    block = {"index": idx, "timestamp": ts, "data": data, "hash": h, "prevHash": last['hash'], "nonce": idx}
    chain.append(block)
    json.dump(chain, open('blockchain.json','w'), indent=2)
    
    print(f"✅ Transfer Success!")
    print(f"   From: {from_addr}")
    print(f"   To: {to_addr}")
    print(f"   Amount: {amount} BCOIN")
    print(f"   Block: #{idx} | Chain: {len(chain)}")
    
    # Auto push
    os.system("git add blockchain.json -f -q && git commit -m 'Transfer {} BCOIN' -q && git push origin main -q".format(amount))
    print(f"   🚀 Live on Explorer!")
    return True

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 transfer.py <from> <to> <amount>")
        print("Example: python3 transfer.py wtanta84 budi 10")
        print("Example: python3 transfer.py BCOIN_ABC123... BCOIN_XYZ... 5")
    else:
        transfer(sys.argv[1], sys.argv[2], sys.argv[3])
