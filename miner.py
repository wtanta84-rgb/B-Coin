import json, time, hashlib

DIFFICULTY = 19
# BITCOIN REAL TARGET - 0000000000000000000

c = json.load(open("blockchain.json"))
ph = c[-1]["hash"]
idx = len(c)

print(f"!!! BITCOIN LEVEL MINING !!!")
print(f"Block {idx} need {'0'*DIFFICULTY}")
print(f"Phone need 1000 YEARS - use at your own risk!")

nonce = 0
start = time.time()
while True:
    raw = f"{idx}{ph}{time.time()}{nonce}"
    h = hashlib.sha256(raw.encode()).hexdigest()
    if h.startswith("0"*DIFFICULTY):
        print(f"FOUND REAL BITCOIN BLOCK! {nonce} {h}")
        c.append({
            "index": idx,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "data": f"BITCOIN LEVEL DIFF {DIFFICULTY} - REAL",
            "previous_hash": ph,
            "hash": h,
            "nonce": nonce
        })
        json.dump(c, open("blockchain.json","w"), indent=2)
        print(f"DONE {len(c)} blocks")
        break
    if nonce % 100000 == 0:
        elapsed = int(time.time()-start)
        print(f"Trying {nonce} - {elapsed}s - still 0.{'0'*5
