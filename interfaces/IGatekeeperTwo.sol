// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

interface IGatekeeperTwo {
    function enter(bytes8 _gateKey) external returns (bool);
}
