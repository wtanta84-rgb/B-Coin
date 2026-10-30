import json, hashlib, time, os
chain = json.load(open('blockchain.json'))
w = json.load(open('wtanta84_wallet.json'))
my_addr = w['address']

def balance_of(addr):
    bal=0
    for b in chain:
        d=b['data']
        if not isinstance(d,dict): continue
        if d.get('to')==addr: bal+=d.get('amount',0)
        if d.get('from')==addr: bal-=d.get('amount',0)
    return bal

bal = balance_of(my_addr)
print(f"Saldo ANTI-BUG: {bal} B-Coin")
to_addr = input("Tujuan: ").strip()
amount = int(input("Jumlah: ").strip())

if amount > bal:
    print(f"❌ GAGAL: Saldo {bal} gak cukup!")
    exit()
if amount <=0:
    print("❌ Jumlah harus >0")
    exit()

new_data = {
  'from': my_addr,
  'to': to_addr,
  'amount': amount,
  'type': 'transfer',
  'timestamp': time.time()
}

print("Mining transfer (PoW 0000) biar anti-bug...")
prev_hash = chain[-1]['hash']
nonce=0
while True:
    h = hashlib.sha256(f"{len(chain)}{prev_hash}{json.dumps(new_data, sort_keys=True)}{nonce}".encode()).hexdigest()
    if h.startswith('0000'):
        break
    nonce+=1

new_block = {
  'index': len(chain),
  'prev_hash': prev_hash,
  'timestamp': time.time(),
  'data': new_data,
  'nonce': nonce,
  'hash': h
}
chain.append(new_block)
open('blockchain.json','w').write(json.dumps(chain, indent=2))
print(f"✅ ANTI-BUG TRANSFER SUKSES!")
print(f"Blok {new_block['index']} | Hash {h[:20]}... | Nonce {nonce}")
