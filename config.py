# B-Coin Config - Scarcity Model
MAX_SUPPLY = 21000000  # 21 Million - Like Bitcoin
HALVING_INTERVAL = 210000  # Halving every 210k blocks
INITIAL_REWARD = 50

def get_reward(block_height):
    halvings = block_height // HALVING_INTERVAL
    reward = INITIAL_REWARD / (2 ** halvings)
    return reward if reward >= 0.01 else 0.01  # Minimum 0.01

def get_supply(block_height):
    supply = 0
    for i in range(block_height):
        supply += get_reward(i)
    return supply

def is_max_reached(block_height):
    return get_supply(block_height) >= MAX_SUPPLY
