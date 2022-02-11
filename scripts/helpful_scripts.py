from brownie import (
    network,
    accounts,
    config,
    interface,
    Contract,
)
from brownie.network.state import Chain
from brownie import web3
from web3 import Web3

def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    return accounts.add(config["wallets"]["from_key"])

def get_new_instance(level_id, player, value=0):
    print("Getting new instance...")
    ethernaut_address = config["networks"][network.show_active()]["ethernaut"]
    level_address = config["networks"][network.show_active()][f"level_{level_id}"]
    ethernaut = interface.IEthernaut(ethernaut_address)
    tx = ethernaut.createLevelInstance(level_address, {"from": player, "value": value})
    tx.wait(1)
    instance_address = tx.events['LevelInstanceCreatedLog']['instance']
    print(f'Deployed new instance at address {instance_address}')
    print()
    return instance_address

def submit_instance(instance_address, player):
    print("Submitting instace...")
    ethernaut_address = config["networks"][network.show_active()]["ethernaut"]
    ethernaut = interface.IEthernaut(ethernaut_address)
    tx = ethernaut.submitLevelInstance(instance_address, {"from": player})
    tx.wait(1)
    print("Level completed!" if tx.events.count('LevelCompletedLog') else "Level not completed...")

def get_web3():
    # this looks terrible...
    return Web3(web3.provider)

def deploy_with_bytecode(abi, bytecode, deployer_account):
    w3 = get_web3()
    contract = w3.eth.contract(abi=abi, bytecode=bytecode)
    nonce = w3.eth.getTransactionCount(str(deployer_account))
    # Submit the transaction that deploys the contract
    transaction = contract.constructor().buildTransaction(
        {
            "chainId": Chain().id,
            "gasPrice": w3.eth.gas_price,
            "from": str(deployer_account),
            "nonce": nonce,
        }
    )
    # Sign the transaction
    signed_txn = w3.eth.account.sign_transaction(transaction, private_key=str(deployer_account.private_key))
    # Send it!
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    # Wait for the transaction to be mined, and get the transaction receipt
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return tx_receipt


