# ethernaut-solutions-brownie

Solutions to smart contract cybersecurity CTF [Ethernaut](https://ethernaut.openzeppelin.com/) written with [Brownie](https://eth-brownie.readthedocs.io/en/stable/). Thanks to Rinkeby testnet forking, it's possible to test solutions quickly on local ganache chain.

# How to run

First add `.env` file to the project directory with the following content:

    export WEB3_INFURA_PROJECT_ID=yourinfuraprojectkey
    export PRIVATE_KEY=yourprivatekey
    
(Replace `yourinfuraprojectkey` and `yourprivatekey` with appropriate values).
    
Then create `rinkeby-fork-dev` network with the following command:

  brownie networks add development rinkeby-fork-dev cmd=ganache-cli host=http://127.0.0.1 fork=https://eth-rinkeby.alchemyapi.io/v2/your_alchemy_key accounts=10 mnemonic=brownie port=8545
  
  (Replace value `your_alchemy_key` with your [Alchemy](https://www.alchemy.com/) key.)

Run:
    brownie compile
  
To solve level e.g. `5` on local ganache chain (Rinkeby fork), run:
  
    brownie run scripts/solve_level_5.py
 
To solve this level on actual Rinkeby testnet run:
    
    brownie run scripts/solve_level_5.py --network rinkeby
  
  After running this command, then going to [Ethernaut](https://ethernaut.openzeppelin.com/) website and connecting with MetaMask (with the account corresponding to the private key from `.env` file), the level should be marked as completed on this website.
  
