from brownie import accounts, config, SimpleStorage, network

# import os

# deploys to a local chain


def deploy_simple_storage():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    print(simple_storage)
    # The above is deploy of a K transaction, which is a state change recognized by Brownie
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    # The above is a call to retrieve initial value followed by an update transaction of the value,
    # indicating from which account
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


# print(account)
# The line below safely calls a 3rd party account and private key safely secured in Brownie it does not push to GIT
# account = accounts.load("freecodecamp-account")
# print(account)
# account = accounts.add(os.getenv("PRIVATE_KEY"))
# print(account)
# account = accounts.add(config["wallets"]["from_key"])
# print(account)


def main():
    deploy_simple_storage()
