from solcx import compile_standard, install_solc
import json
from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()

install_solc("0.6.0")

# Compile Our Solidity

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                }
            }
        },
    },
    solc_version="0.6.0",
)

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# get byecode
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]

# get abi
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# for connecting to ganache local blockchain
# w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:8545"))
# chain_id = 1337
# my_address = "0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1"
# private_key = os.getenv("PRIVATE_KEY")

# for connecting to 3rd party chain
w3 = Web3(
    Web3.HTTPProvider("https://sepolia.infura.io/v3/e19872112bce43e1912a1bc08cf948e0")
)
chain_id = 11155111
my_address = "0x7368F408E4F837403890A6A3bBc3cFC4E2c88441"
private_key = os.getenv("PRIVATE_KEY")

# Create the contract in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
# Get the latestest transaction
nonce = w3.eth.getTransactionCount(my_address)
print(nonce)

# SENDING A TRANSACTION TO A LOCAL BLOCKCHAIN
# 1. Build a transaction
# 2. Sign a transaction
# 3. Send a transaction
transaction = SimpleStorage.constructor().buildTransaction(
    {"chainId": chain_id, "from": my_address, "nonce": nonce}
)

signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
# Send the transaction
print("Deploying K...")
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
print(tx_hash)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(tx_receipt)
print("Deployed")

# Working with the K, you always need
# K Address
# K ABI
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
# sometimes people will create an abi file e.g abi.json or abi.py
# 2 ways to make a transaction with a blockchain
# 1. Call - simulate a transaction on a blockchain but do not make a state change
# 2. Transaction - Acutally make a state change (building & sending a transaction)

# Intial value of favorite number
print(simple_storage.functions.retrieve().call())
print("Updating K...")
print(simple_storage.functions.store(15).call())

# if we want to store something using the transaction then we have to go thru the same process as when we deployed the txn
store_transaction = simple_storage.functions.store(15).buildTransaction(
    {"chainId": chain_id, "from": my_address, "nonce": nonce + 1}
)

signed_store_txn = w3.eth.account.sign_transaction(
    store_transaction, private_key=private_key
)
send_store_tx = w3.eth.send_raw_transaction(signed_store_txn.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(send_store_tx)

print(simple_storage.functions.retrieve().call())
print("Updated!")
