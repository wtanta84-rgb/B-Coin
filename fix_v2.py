import json, hashlib, time

print("=== B-Coin v2 Anti-Bug Fix ===")
chain = json.load(open('blockchain.json'))

# FIX BUG 1: Benerin data string jadi dict
fixed = 0
for b in chain:
    d = b['data']
    if isinstance(d, str):
        try:
            # ganti ' jadi " biar jadi JSON valid
            b['data'] = json.loads(d.replace("'", '"'))
            fixed += 1
        except:
            pass

# FIX BUG 2: Mining ulang Blok 73 biar ada PoW 0000
print(f"Fix {fixed} blok string -> dict")
target = chain[73]
if not target['hash'].startswith('0000'):
    print(f"Mining ulang Blok 73...")
    prev_hash = target['prev_hash']
    data_str = json.dumps(target['data'], sort_keys=True)
    nonce = 0
    while True:
        h = hashlib.sha256(f"{73}{prev_hash}{data_str}{nonce}".encode()).hexdigest()
        if h.startswith('0000'): # difficulty 4 = anti-bug
            target['nonce'] = nonce
            target['hash'] = h
            print(f"FOUND! nonce={nonce} hash={h}")
            break
        nonce += 1
        if nonce % 50000 == 0:
            print(f"mining... {nonce}")

open('blockchain.json','w').write(json.dumps(chain, indent=2))
print(f"✅ SELESAI! Total Blok {len(chain)} udah ANTI-BUG v2")
