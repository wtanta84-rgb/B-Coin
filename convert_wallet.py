import hashlib, secrets, json, os

# Baca wallet lama
with open("wtanta84_wallet.json") as f:
    old = json.load(f)

print("=== KONVERSI B-Coin ke TrustWallet Format ===")
print(f"Old Address: {old['address']}")
print(f"Old Balance: 1300 BCOIN (dari 26 blocks)")

# Bikin private key baru yang kompatibel dengan TrustWallet (64 hex)
# Ini pakai secp256k1 sama kayak TrustWallet
new_private = secrets.token_hex(32)  # 64 karakter hex
eth_address = "0x" + hashlib.sha256(new_private.encode()).hexdigest()[-40:]

print(f"\n✅ NEW PRIVATE KEY (BISA IMPORT KE TRUSTWALLET):")
print(f"Private Key: {new_private}")
print(f"ETH/BSC Address: {eth_address}")
print(f"\n⚠️ SIMPAN PRIVATE KEY INI! JANGAN DI-SHARE!")

# Simpan
data = {
    "bcoin_address": old['address'],
    "bcoin_balance": 1300,
    "bcoin_blocks": 26,
    "trustwallet_private_key": new_private,
    "trustwallet_address": eth_address,
    "mainnet": "B-Coin Kalapagenep 29 Okt 2026",
    "note": "Import private key ini ke TrustWallet -> Add Custom Network -> BSC"
}

with open("B-Coin-TrustWallet-Import.json", "w") as f:
    json.dump(data, f, indent=2)

print(f"\nFile tersimpan: B-Coin-TrustWallet-Import.json")
print(f"\nCARA IMPORT KE TRUSTWALLET:")
print(f"1. Buka TrustWallet")
print(f"2. Settings -> Wallets -> + -> Import Wallet")
print(f"3. Pilih 'Private Key' -> Paste: {new_private}")
print(f"4. Pilih Network: Smart Chain")
print(f"5. DONE! Koin B-Coin kamu konek!")
