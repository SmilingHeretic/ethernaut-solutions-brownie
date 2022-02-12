// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

interface IShop {
    function price() external returns (uint256);

    function isSold() external view returns (bool);

    function buy() external;
}
