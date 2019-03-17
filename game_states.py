"""States related to the game."""

from enum import Enum


class GameStates(Enum):
    """States related to the game."""

    PLAYERS_TURN = 1
    ENEMY_TURN = 2
    PLAYER_DEAD = 3
