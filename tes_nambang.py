import json, time, hashlib, os, subprocess
print("🔥 TES NAMBANG 5 BLOCK - LIHAT PUSH NYA BOS!")
for i in range(5):
    # Load
    chain=json.load(open('blockchain.json'))
    last=chain[-1]
    new=len(chain)
    data={"from":f"miner_{new}","to":"wtanta84","amount":50}
    ts=int(time.time()*1000)
    h=hashlib.sha256(f"{new}{last['hash']}{ts}{str(data)}".encode()).hexdigest()
    chain.append({"index":new,"timestamp":ts,"data":data,"hash":h,"prevHash":last['hash'],"nonce":new})
    json.dump(chain, open('blockchain.json','w'), indent=2)
    print(f"\n[Block {new}] Chain jadi {len(chain)}")

    # Push TANPA --quiet biar keliatan
    print("-> PUSH ke GitHub...")
    os.system("cd ~/B-Coin && git add blockchain.json -f && git commit -m 'TEST Block {}' 2>&1 | tail -2".format(len(chain)))
    result = subprocess.getoutput("cd ~/B-Coin && git push origin main 2>&1")
    print(result)
    if "main -> main" in result or "up to date" not in result.lower():
        print("✅ PUSH SUKSES! CEK: raw.githubusercontent.com/wtanta84-rgb/B-Coin/main/blockchain.json")
    else:
        print("❌ PUSH GAGAL! ADA ERROR DI ATAS!")
        if "Authentication" in result or "403" in result or "remote:" in result:
            print("TOKEN EXPIRED BOS! Perlu login ulang!")
    time.sleep(4)

print("\n=== SELESAI TES 5 BLOCK ===")
print("CEK GITHUB SEKARANG:")
os.system("curl -s https://raw.githubusercontent.com/wtanta84-rgb/B-Coin/main/blockchain.json | python3 -c \"import json,sys; d=json.load(sys.stdin); print(f'GitHub: {len(d)} blocks')\"")
