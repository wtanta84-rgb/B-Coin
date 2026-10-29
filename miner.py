import time
from core import Block, B_Coin
coin = B_Coin()
print("Mining B-Coin terus... CTRL+C untuk stop")
num = 2
while True:
    try:
        coin.add_block({"from": f"miner_{num}", "to": "wtanta84", "amount": 50})
        print(f"Total Supply: {num*50} B-Coin")
        num+=1
        time.sleep(1)
    except KeyboardInterrupt:
        break
