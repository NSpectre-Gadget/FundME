//SPDX-License-Indentifier:MIT
pragma solidity ^0.6.6;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract Lottery {
    address payable[] public players;
    uint256 public usdEntryFee;
    AggregatorV3Interface internal ethUsdPriceFeed;

    constructor() public {
        usdEntryFee = 50 * (10 ** 18);
        ethUsdPriceFeed = AggregatorV3Interface(_priceFeedAddress);
    }

    function enter() public payable {
        // $50 minimum
        require();
        players.push(msg.sender);
    }

    function getEntranceFee() public view returns (uint256) {
        // * Returns the latest answer.
        // prettier-ignore
        (
            /* uint80 roundID */,
            int256 answer,
            /*uint startedAt*/,
            /*uint timeStamp*/,
            /*uint80 answeredInRound*/
        ) = ethUsdPriceFeed.latestRoundData();
        uint256 adjustedPrice = uint256(price) * 10 ** 10; //18  decimals
        // $50, $2,000 / ETH
        // 50/2,000
        // 50 * 100000 / 2000
        uint256 costToEnter = (usdEntryFee * 10 ** 18) / adjustedPrice;
        return costToEnter;
    }

    function startLottery() public {}

    function endLottery() public {}
}
/// @notice Explain to an end user what this does
/// @dev Explain to a developer any extra details
/// @return Documents the return variables of a contract’s function state variable
/// @inheritdoc	Copies all missing tags from the base function (must be followed by the contract name)player
