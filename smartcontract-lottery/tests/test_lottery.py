# 
#
from brownie import Lottery, accounts, config, network
from web3 import Web3

def test_get_entrance_fee():
    account = accounts[0]
    lottery = Lottery.deploy(config["network"][network.showactive()]["eth_usd_price_feed"], {"from": account})
    #assert lottery.entranceFee()>18000000000000000000
    assert lottery.getEntranceFee() > Web3.toWei(0.019, "ether")
    assert lottery.getEntranceFee() < Web3.toWei(0.027, "ether")
    
