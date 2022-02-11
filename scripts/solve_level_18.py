from brownie import (
    network,
    accounts,
    config,
    interface,
    history,
    Contract,
    Solver
)
from scripts.helpful_scripts import (
    get_account,
    get_new_instance,
    submit_instance,
    deploy_with_bytecode,
)
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()


def main():
    player = get_account()
    instance_address = get_new_instance(level_id=18, player=player)

    bytecode = "0x600a80600d6000396000f300fe602a60805260206080f3"
    
    tx_receipt = deploy_with_bytecode(Solver.abi, bytecode, player)
    print(Solver.at(tx_receipt.contractAddress).whatIsTheMeaningOfLife())

    if network.show_active() == "rinkeby":
        network.disconnect()
        network.connect("rinkeby")

    player = get_account()
    magic_num_contract = interface.IMagicNum(instance_address)
    tx = magic_num_contract.setSolver(tx_receipt.contractAddress, {"from": player})
    tx.wait(1)

    submit_instance(instance_address, player)
