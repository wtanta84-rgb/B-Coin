#!/data/data/com.termux/files/usr/bin/bash
cd ~/B-Coin
termux-wake-lock
pkill -f miner_sync
nohup python3 miner_sync.py > miner_sync.log 2>&1 &
echo "MINER AUTO-SYNC JALAN!"
sleep 1
tail -f miner_sync.log
