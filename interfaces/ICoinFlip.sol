// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

interface ICoinFlip {
    function consecutiveWins() external view returns (uint256);

    function flip(bool _guess) external returns (bool);
}
