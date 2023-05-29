from brownie import accounts, config, SimpleStorage
# import os

# deploys to a local chain


def deploy_simple_storeage():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)
    # print(account)
    # account = accounts.load("freecodecamp-account")
    # print(account)
    # account - accunts.add(os.getenv("PRIVATE_KEY"))
    # print(account)
    # account - accounts.add(config["wallets"]["from_key"])
    # print(account)


def main():
    deploy_simple_storeage()
