"""CSC111 Winter 2023 Group Project: PlayPal

Instructions
===============================

This Python module contains the main dataclasses we use for PlayPal

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of the
Department of Computer Science at the University of Toronto St. George campus.
All forms ofvdistribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for any code we have written
for CSC111, please consult the Course Syllabus.

This file is Copyright (c) 2023 Levent Ozay, Ivan Kraskov.
"""

from __future__ import annotations
from dataclasses import dataclass


@dataclass
class GameNode:
    """
    A GameNode class that represents a game.

    Instance Attributes:
        - genres: the genres of the Game
        - name: the name of the Game
        - rating: the rating of the game represented as a number.
        - mature: defines if the game for mature audiences or not
        - achievements: Are there any achievements in the game?
        - min_req: the minimum requirements for the game
        - rec_req: the recommended requirements for the game
        - price: the price of the game as a float.
        - single_player: is the game single player?
        - multi_player: is the game multiplayer?
        - year: the year the game was released
    """
    genres: list
    name: str
    rating: int
    mature: bool
    achievements: bool
    min_req: str
    rec_req: str
    price: float
    single_player: bool
    multi_player: bool
    year: int


class GameTree:
    """A decision tree for our project.

    There are 2 types of nodes:
        - Game Node
        - a usual node represented as a simple string.
        - a "bundle" node which is a set of genres

    Instance Attributes:
        - node: the node, a root which is either a parameter or a game in our decision tree
    """
    node: str | GameNode

    # Private Instance Attributes:
    #  - _subtrees: The subtrees. str refers to the name of the game or a parameter.
    _subtrees: dict[str, GameTree]

    def __init__(self, node: GameNode | str = "*") -> None:
        """Initialize a new game tree.
        Note that this initializer uses optional arguments.
        """
        self.node = node
        self._subtrees = {}

    def get_subtrees(self) -> dict:
        """Return the subtrees of this game tree."""
        return self._subtrees

    def add_subtree(self, subtree: GameTree) -> None:
        """Add a subtree to this game tree."""
        if isinstance(subtree.node, GameNode):
            self._subtrees[subtree.node.name] = subtree
        else:
            self._subtrees[subtree.node] = subtree


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (In PyCharm, select the lines below and press Ctrl/Cmd + / to toggle comments.)
    # You can use "Run file in Python Console" to run PythonTA,
    # and then also test your methods manually in the console.
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 120,
        'extra-imports': [''],
        'disable': ['unused-import', 'too-many-instance-attributes']
    })
