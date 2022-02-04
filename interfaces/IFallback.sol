// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

interface IFallback {
    function contribute() external payable;

    function getContribution() external view returns (uint256);

    function withdraw() external;

    function nonExistentFunction() external;

    receive() external payable;
}
