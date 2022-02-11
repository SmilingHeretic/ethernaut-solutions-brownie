// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

interface ISimpleToken {
    function destroy(address payable _to) external;
}
