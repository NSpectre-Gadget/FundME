pragma solidity ^0.6.6;

contract Lottery {

    address payable[] public players;
    uint256 public usdEntryFee;
    AggregatorV3Interface internal ethUsdPriceFeed;

    constructor() public {
        usdEntryFee = 50 * (10**18);
        ethUsdPriceFeed = AggregatorV3Interface(_priceFeedAddress);
    }


    function enter() public payable {
        // $50 minimum
        require();
        players.push(msg.sender);
    }

    function getEntranceFee() public (uint 256) {
        // ?
    }

    function startLottery() public {}

    function endLottery() public {}
}
/// @notice Explain to an end user what this does
/// @dev Explain to a developer any extra details
/// @return Documents the return variables of a contract’s function state variable
/// @inheritdoc	Copies all missing tags from the base function (must be followed by the contract name)player
