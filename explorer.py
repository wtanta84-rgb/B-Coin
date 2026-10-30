import json, os
from core import B_Coin

coin = B_Coin()
print("\n" + "="*50)
print("🔍 B-COIN BLOCK EXPLORER - Kalapagenep Mainnet")
print("="*50)
print(f"Genesis: {coin.chain[0].hash[:20]}...")
print(f"Total Blocks: {len(coin.chain)}")
print(f"Total Supply: {len(coin.chain)*50} B-Coin")
print(f"Wallet: B5ac0296b73cb6469ace0312e622de830bf")
print(f"Status: LIVE ✅")
print("="*50)

# Cek blockchain file kalau ada
if os.path.exists("blockchain.json"):
    with open("blockchain.json") as f:
        data = json.load(f)
        print(f"\nSaved Blocks: {len(data)}")

print("\nLast 3 Blocks:")
for block in coin.chain[-3:]:
    print(f" #{block.index} | Hash: {block.hash[:30]}... | Nonce: {block.nonce}")

print("\nExplorer ready! Share: github.com/wtanta84-rgb/B-Coin")
