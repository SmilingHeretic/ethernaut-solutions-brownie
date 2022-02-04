from brownie import (
    network,
    accounts,
    config,
    interface,
    Contract,
)

def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    return accounts.add(config["wallets"]["from_key"])

def get_new_instance(level_id, player):
    print(f'Player address {player}')
    ethernaut_address = config["networks"][network.show_active()]["ethernaut"]
    level_address = config["networks"][network.show_active()][f"level_{level_id}"]
    print(f'Level addres {level_address}')
    ethernaut = interface.IEthernaut(ethernaut_address)
    print("Getting new instance...")
    tx = ethernaut.createLevelInstance(level_address, {"from": player})
    tx.wait(1)
    instance_address = tx.events['LevelInstanceCreatedLog']['instance']
    print(f'Deployed new instance at addres {instance_address}')
    return instance_address

def submit_instance(instance_address, player):
    print(f'Player address {player}')
    ethernaut_address = config["networks"][network.show_active()][f"ethernaut"]
    print(f'Instance address {instance_address}')
    ethernaut_address = config["networks"][network.show_active()]["ethernaut"]
    print("Submitting instace...")
    ethernaut = interface.IEthernaut(ethernaut_address)
    tx = ethernaut.submitLevelInstance(instance_address, {"from": player})
    tx.wait(1)
    print("Level completed!" if tx.events.count('LevelCompletedLog') else "Level not completed...")
