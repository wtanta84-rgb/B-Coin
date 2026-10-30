import json
from config import MAX_SUPPLY, get_reward, get_supply
chain=json.load(open('blockchain.json'))
idx=len(chain)
supply=get_supply(idx)
reward=get_reward(idx)
print(f"📊 B-Coin Supply Status")
print(f"   Blocks Mined: {idx}")
print(f"   Current Reward: {reward} BCOIN/block")
print(f"   Current Supply: {supply:.2f} / {MAX_SUPPLY:,} BCOIN")
print(f"   Remaining: {MAX_SUPPLY-supply:.2f}")
print(f"   Progress: {supply/MAX_SUPPLY*100:.6f}%")
print(f"   Halving: Every 210,000 blocks")
print(f"   Next Halving at: {(idx//210000+1)*210000} blocks")
