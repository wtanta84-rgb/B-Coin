import json, time, hashlib, os, subprocess
from config import MAX_SUPPLY, get_reward, get_supply, is_max_reached

print("🔥 B-Coin Scarce Miner - Max Supply 21M - Halving Enabled")
print(f"Max Supply: {MAX_SUPPLY:,} BCOIN")
print("Press CTRL+C to stop\n")

while True:
    try:
        chain=json.load(open('blockchain.json'))
        idx=len(chain)
        
        if is_max_reached(idx):
            print(f"🛑 MAX SUPPLY REACHED! {MAX_SUPPLY:,} BCOIN - Mining Stopped!")
            break
        
        reward = get_reward(idx)
        supply = get_supply(idx)
        remaining = MAX_SUPPLY - supply
        
        last=chain[-1]
        data={"from":f"miner_{idx}","to":"wtanta84","amount":reward, "reward":reward}
        ts=int(time.time()*1000)
        h=hashlib.sha256(f"{idx}{last['hash']}{ts}{str(data)}{idx}".encode()).hexdigest()
        chain.append({"index":idx,"timestamp":ts,"data":data,"hash":h,"prevHash":last['hash'],"nonce":idx})
        json.dump(chain, open('blockchain.json','w'), indent=2)
        
        progress = supply / MAX_SUPPLY * 100
        print(f"⛏️ Block #{idx} | Reward {reward} | Supply {supply:.2f}/{MAX_SUPPLY:,} ({progress:.6f}%) | Remaining {remaining:.2f} | Chain {len(chain)}")
        
        os.system(f"cd ~/B-Coin && git add blockchain.json -f -q && git commit -m 'Block {len(chain)} Reward {reward}' -q")
        out=subprocess.getoutput("cd ~/B-Coin && git push origin main 2>&1")
        if "main -> main" in out:
            print(f"   ✅ LIVE ON EXPLORER!")
        time.sleep(3)
    except KeyboardInterrupt:
        print("\n🛑 Stopped!"); break
