from brownie import (
    network,
    accounts,
    config,
    interface,
    Contract,
    Building,
)
from scripts.helpful_scripts import (
    get_account,
    get_new_instance,
    submit_instance,
)
from web3 import Web3


def main():
    player = get_account()
    instance_address = get_new_instance(level_id=11, player=player)

    elevator_contract = interface.IElevator(instance_address)
    building_contract = Building.deploy(elevator_contract, {"from": player})

    tx = building_contract.goToLastFloor({"from": player})
    tx.wait(1)

    submit_instance(instance_address, player)
