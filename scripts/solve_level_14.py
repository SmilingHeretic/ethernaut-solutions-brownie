from brownie import (
    network,
    accounts,
    config,
    interface,
    Contract,
    GatekeeperTwoAttack
)
from scripts.helpful_scripts import (
    get_account,
    get_new_instance,
    submit_instance,
)
from web3 import Web3


def main():
    player = get_account()
    instance_address = get_new_instance(level_id=14, player=player)

    attack_contract = GatekeeperTwoAttack.deploy(instance_address, {"from": player, "allow_revert": True})

    submit_instance(instance_address, player)