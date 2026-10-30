# B-Coin - Mainnet v2.0

B-Coin adalah cryptocurrency open-source asli Indonesia dari Kalapagenep.

## Genesis Block
- Tanggal: 29 Oktober 2026
- Lokasi: Kalapagenep, Jawa Barat
- Total Supply: 21,000,000 B-Coin
- Consensus: Proof of Work
- Premine: 0 (Fair Launch)

## Roadmap
- [x] v1.0 Mainnet Launch
- [ ] Wallet Android
- [ ] Mining App

## Cara Menjalankan Node
python3 core.py



cd ~/B-Coin
cat > README.md << 'MD'
# 🪙 B-Coin - 100% Transparent Blockchain

**Live Explorer:** https://wtanta84-rgb.github.io/B-Coin/  
**Blockchain Raw Data:** https://raw.githubusercontent.com/wtanta84-rgb/B-Coin/main/blockchain.json  
**Location:** Bandung, West Java, Indonesia

---
cd ~/B-Coin

# === 1. TERMUX MINER (Phone) ===
cat > nambang.py << 'PY'
import json, time, hashlib, os, subprocess
print("🔥 B-Coin Termux Miner + Auto Explorer - wtanta84")
print("Press CTRL+C to stop\n")
while True:
    try:
        chain=json.load(open('blockchain.json')); last=chain[-1]; idx=len(chain)
        data={"from":f"miner_{idx}","to":"wtanta84","amount":50}
        ts=int(time.time()*1000)
        h=hashlib.sha256(f"{idx}{last['hash']}{ts}{str(data)}{idx}".encode()).hexdigest()
        chain.append({"index":idx,"timestamp":ts,"data":data,"hash":h,"prevHash":last['hash'],"nonce":idx})
        json.dump(chain, open('blockchain.json','w'), indent=2)
        print(f"⛏️ Block #{idx} | Chain {len(chain)} | Hash {h[:12]}...")
        os.system(f"cd ~/B-Coin && git add blockchain.json -f -q && git commit -m 'Block {len(chain)}' -q")
        out=subprocess.getoutput("cd ~/B-Coin && git push origin main 2>&1")
        print("   ✅ LIVE ON EXPLORER!" if "main -> main" in out else f"   ❌ PUSH FAILED: {out[:60]}")
        time.sleep(3)
    except KeyboardInterrupt:
        print("\n🛑 Stopped!"); break
PY

# === 2. BASIC MINING (Local Only) ===
cat > mining_biasa.py << 'PY'
import json, time, hashlib
print("⛏️ B-Coin Basic Miner - Local Only")
print("Press CTRL+C to stop\n")
while True:
    chain=json.load(open('blockchain.json')); last=chain[-1]; idx=len(chain)
    data={"from":f"miner_{idx}","to":"wtanta84","amount":50}; ts=int(time.time()*1000)
    nonce=0
    while True:
        h=hashlib.sha256(f"{idx}{last['hash']}{ts}{data}{nonce}".encode()).hexdigest()
        if h.startswith("00"): break
        nonce+=1
    chain.append({"index":idx,"timestamp":ts,"data":data,"hash":h,"prevHash":last['hash'],"nonce":nonce})
    json.dump(chain, open('blockchain.json','w'), indent=2)
    print(f"✅ Block #{idx} | Hash {h[:16]} | Nonce {nonce} | Chain {len(chain)}")
    time.sleep(1)
PY

# === 3. LAPTOP MINER (Windows/Mac/Linux) ===
cat > mine_laptop.py << 'PY'
import json, time, hashlib, os, subprocess, json as js
print("💻 B-Coin Laptop Miner - 10x Faster than Phone")
print("Mining to: wtanta84 | Auto Push to Explorer\n")
while True:
    try:
        chain=js.load(open('blockchain.json')); last=chain[-1]; idx=len(chain)
        data={"from":f"laptop_miner_{idx}","to":"wtanta84","amount":50}
        ts=int(time.time()*1000); nonce=0; start=time.time()
        while True:
            raw=f"{idx}{last['hash
