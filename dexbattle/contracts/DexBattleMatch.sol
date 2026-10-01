// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

/// @title DexBattleMatch
/// @notice Minimal match-lifecycle reference for a competitive Web3 game.
/// @dev Portfolio reference only; settlement/oracle design requires an audit.
contract DexBattleMatch {
    enum State { Open, Active, Settled, Cancelled }

    struct MatchInfo {
        address creator;
        address opponent;
        uint256 stake;
        State state;
        address winner;
    }

    uint256 public nextMatchId;
    mapping(uint256 => MatchInfo) public matches;

    event MatchCreated(uint256 indexed id, address indexed creator, uint256 stake);
    event MatchJoined(uint256 indexed id, address indexed opponent);
    event MatchSettled(uint256 indexed id, address indexed winner);
    event MatchCancelled(uint256 indexed id);

    function createMatch() external payable returns (uint256 id) {
        require(msg.value > 0, "stake required");
        id = nextMatchId++;
        matches[id] = MatchInfo(msg.sender, address(0), msg.value, State.Open, address(0));
        emit MatchCreated(id, msg.sender, msg.value);
    }

    function joinMatch(uint256 id) external payable {
        MatchInfo storage m = matches[id];
        require(m.state == State.Open, "not open");
        require(msg.sender != m.creator, "creator cannot join");
        require(msg.value == m.stake, "incorrect stake");
        m.opponent = msg.sender;
        m.state = State.Active;
        emit MatchJoined(id, msg.sender);
    }

    /// @dev Production systems should authorize settlement through a robust,
    /// independently reviewed game-result/oracle mechanism.
    function settle(uint256 id, address winner) external {
        MatchInfo storage m = matches[id];
        require(m.state == State.Active, "not active");
        require(winner == m.creator || winner == m.opponent, "invalid winner");
        m.winner = winner;
        m.state = State.Settled;
        emit MatchSettled(id, winner);
        (bool ok,) = winner.call{value: address(this).balance >= m.stake * 2 ? m.stake * 2 : address(this).balance}("");
        require(ok, "payout failed");
    }
}
