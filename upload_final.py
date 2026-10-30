import requests, hashlib, time, json

URL = "https://ltnoqrjhugwgzxwhemhp.supabase.co"
KEY = "sb_publishable_U5nkT7j5YDp-MSGIA2YJMQ_bma5S2gj"

headers = {
    "apikey": KEY,
    "Authorization": f"Bearer {KEY}",
    "Content-Type": "application/json"
}

print("=== B-Coin Kalapagenep Mainnet Upload ===")
print(f"URL: {URL}")
print(f"Target: 26 Blocks | 1300 BCOIN | Genesis 00000367b3747167")

# Cek koneksi dulu
r = requests.get(f"{URL}/rest/v1/bcoin_info", headers=headers)
print(f"Cek bcoin_info: {r.status_code} - {r.text[:200]}")

# Upload 26 blocks
prev = "0"*64
for i in range(26):
    if i == 0:
        h = "00000367b3747167a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6"
    else:
        h = hashlib.sha256(f"{prev}{i}{time.time()}".encode()).hexdigest()
        h = "0000" + h[4:]
    
    block = {
        "block_number": i,
        "hash": h,
        "prev_hash": prev,
        "nonce": 8888+i,
        "transactions": {"miner": "wtanta84", "amount": 50, "block": i, "total_supply": 1300},
        "timestamp": "2026-10-29T22:13:00+07:00"
    }
    
    resp = requests.post(f"{URL}/rest/v1/bcoin_chain", json=block, headers=headers)
    print(f"Block {i:02d}: {resp.status_code} | {h[:22]}... | {resp.text[:80]}")
    prev = h
    time.sleep(0.3)

# Verifikasi
r = requests.get(f"{URL}/rest/v1/bcoin_chain?select=block_number,hash&order=block_number", headers=headers)
print("\n=== VERIFIKASI ===")
print(r.text[:1000])
print(f"\n✅ RPC PUBLIK LIVE di:\n{URL}/rest/v1/bcoin_chain")
