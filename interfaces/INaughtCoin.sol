// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

interface INaughtCoin {
    function approve(address spender, uint256 amount) external returns (bool);

    function balanceOf(address account) external view returns (uint256);

    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) external returns (bool);
}
