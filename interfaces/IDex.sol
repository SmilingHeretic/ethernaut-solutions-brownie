// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

interface IDex {
    function token1() external view returns (address);

    function token2() external view returns (address);

    function swap(
        address from,
        address to,
        uint256 amount
    ) external;

    function add_liquidity(address token_address, uint256 amount) external;

    function get_swap_price(
        address from,
        address to,
        uint256 amount
    ) external view returns (uint256);

    function approve(address spender, uint256 amount) external;

    function balanceOf(address token, address account)
        external
        view
        returns (uint256);
}
