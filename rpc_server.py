from flask import Flask, jsonify, request
import json, os

app = Flask(__name__)

def load_chain():
    if os.path.exists("blockchain.json"):
        with open("blockchain.json") as f:
            return json.load(f)
    return []

@app.route('/')
def info():
    chain = load_chain()
    return jsonify({
        "name": "B-Coin Mainnet",
        "chainId": 8888,
        "network": "Kalapagenep",
        "blocks": len(chain),
        "supply": "1300 BCOIN",
        "genesis": chain[0]['hash'] if chain else None,
        "founder": "wtanta84-rgb",
        "rpc_url": "https://b-coin-rpc... (akan online)",
        "status": "LIVE MAINNET - 29 Okt 2026"
    })

@app.route('/rpc', methods=['POST'])
def rpc():
    data = request.get_json()
    method = data.get('method')
    chain = load_chain()
    
    if method == "eth_chainId":
        return jsonify({"jsonrpc":"2.0","id":1,"result":"0x22b8"}) # 8888
    if method == "eth_blockNumber":
        return jsonify({"jsonrpc":"2.0","id":1,"result": hex(len(chain))})
    if method == "eth_getBalance":
        return jsonify({"jsonrpc":"2.0","id":1,"result": hex(1300 * 10**18)})
    if method == "bcoin_getBlocks":
        return jsonify({"jsonrpc":"2.0","id":1,"result": chain})
    
    return jsonify({"jsonrpc":"2.0","id":1,"result":"B-Coin RPC Active"})

if __name__ == '__main__':
    print("=== B-Coin RPC Server ===")
    print("Mainnet: 26 Blocks | 1300 BCOIN")
    print("ChainID: 8888")
    print("RPC Running on http://0.0.0.0:5000")
    print("\nUntuk konek ke MetaMask/TrustWallet:")
    print("Network Name: B-Coin Mainnet")
    print("RPC URL: http://IP_KAMU:5000/rpc")
    print("ChainID: 8888")
    print("Symbol: BCOIN")
    app.run(host='0.0.0.0', port=5000)
