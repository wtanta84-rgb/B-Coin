import json

chain = json.load(open('blockchain.json'))
my_addr_new = "B6db491c1b392ef11cb71a13ae005c26c"
my_addr_old = "Bc1a40d919f6ef5813285638b7c2830d0"

def balance_of(addr):
    bal = 0
    for b in chain:
        d = b['data']
        if not isinstance(d, dict): continue
        if d.get('to') == addr or d.get('to') == 'wtanta84':
            bal += d.get('amount',0)
        if d.get('from') == addr:
            bal -= d.get('amount',0)
    return bal

print("=== B-Coin v2 Wallet Anti-Bug ===")
print(f"Wallet BARU (B6db49...): {balance_of(my_addr_new)} B-Coin")
print(f"Wallet LAMA (Bc1a40...): {balance_of(my_addr_old)} B-Coin")
print(f"Total Supply: {balance_of(my_addr_new) + balance_of(my_addr_old) + 2550} (harus 6150 kalau bener)")
# Validasi chain
ok = True
for i in range(1,len(chain)):
    if chain[i]['prev_hash'] != chain[i-1]['hash']:
        print(f"❌ Chain putus di blok {i}")
        ok=False
if ok:
    print("✅ Chain VALID, prev_hash nyambung semua!")
