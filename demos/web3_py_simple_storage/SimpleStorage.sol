pragma solidity ^0.6.0;

contract SimpleStorage {
    // this will get initialized to 0!
    uint256 public favoriteNumber;

    struct People {
        uint256 favoriteNumber;
        string name;
    }

    People[] public people;
    mapping(string => uint256) public nameToFavoriteNumber;

    function store(uint256 _favoriteNumber) public returns (uint256) {
        favoriteNumber = _favoriteNumber;
        return _favoriteNumber;
    }

    function retrieve() public view returns (uint256) {
        return favoriteNumber;
    }

    function addPersons(string memory _name, uint256 _favoriteNumber) public {
        //The below pushes the struct combination to the open array container above
        people.push(People({favoriteNumber: _favoriteNumber, name: _name}));
        //The below ties to the mapping line above; Note it does not make a state change
        nameToFavoriteNumber[_name] = _favoriteNumber;
    }
}
