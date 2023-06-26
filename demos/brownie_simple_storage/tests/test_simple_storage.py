from brownie import SimpleStorage, accounts, network, config


def test_deploy():
    # Arrange
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    # Assert
    assert starting_value == expected


def test_updating_storage():
    # Arrange
    account = account()
    simple_storage = SimpleStorage.deploy({"from": account})
    # Act
    expected = 15
    simple_storage.store(expected, ({"from": account}))
    # Assert
    assert expected == simple_storage.retrieve()


# def get_account():
# if network.show_active() == "development":
#    return accounts[0]
# else:
#    return accounts.add(config["wallets"]["from_key"])
