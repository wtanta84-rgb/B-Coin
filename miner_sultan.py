import json, time, os, hashlib, datetime
print("🚀 MINER SULTAN ANTI MENTOK JALAN!")
num=0
while True:
  try:
    with open('blockchain.json','r') as f:
      chain=json.load(f)
    last=chain[-1]
    new_index=len(chain)
    new_data={"from":f"miner_{new_index}", "to":"wtanta84", "amount":50}
    ts=int(time.time()*1000)
    # hash simple
    h=hashlib.sha256(f"{new_index}{last['hash']}{ts}{json.dumps(new_data)}".encode()).hexdigest()
    new_block={"index":new_index,"timestamp":ts,"data":new_data,"hash":h,"prevHash":last['hash'],"nonce":new_index}
    chain.append(new_block)
    with open('blockchain.json','w') as f:
      json.dump(chain,f,indent=2)
    print(f"Block {new_index} -> wtanta84 +50 | Chain {len(chain)} | Hash {h[:15]}...")
    num+=1
    if num%3==0:
      print("⏫ PUSH KE EXPLORER...")
      os.system("cd ~/B-Coin && git add blockchain.json && git commit -m 'AUTO Block {}' --quiet && git push origin main --quiet".format(len(chain)))
      print("✅ MASUK EXPLORER! Cek wtanta84-rgb.github.io/B-Coin/")
    time.sleep(3)
  except Exception as e:
    print(f"Error: {e}")
    time.sleep(2)
