"""CSC111 Winter 2023 Group Project: PlayPal

Instructions
===============================

This Python module contains the load_game_tree function for the PlayPal program, which is used to create a game tree
from a dictionary. In addition, this file contains the make_suggestions function, which is used to make suggestions
for the user
Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of the
Department of Computer Science at the University of Toronto St. George campus.
All forms ofvdistribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for any code we have written
for CSC111, please consult the Course Syllabus.

This file is Copyright (c) 2023 Levent Ozay, Ivan Kraskov, Defne Tuncer, Gavin William Burnham.
"""

from __future__ import annotations
import random
import tree


def load_game_tree(games_file: dict) -> tree.GameTree:
    """Return a new game treee based on games_file.

    Preconditions:
        - games_file is a dictionary with the keys 'Genres' and 'Games'.
        The key 'Genres' maps to a set of strings, while the key 'Games' maps to a list of GameNode objects.

    """
    genres = games_file['Genres']
    games = games_file['Games']
    treee = tree.GameTree()
    games.sort(key=lambda x: x.rating)  # sorts the games by rating

    #  Add subtree genres and Mature/Not Mature subtrees.
    for genre in genres:
        gen = tree.GameTree(genre)
        mature_tree = tree.GameTree("Mature")
        not_mature_tree = tree.GameTree("Not Mature")
        single_player = tree.GameTree("Single-Player")
        multi_player = tree.GameTree("Multi-Player")
        mature_tree.add_subtree(single_player)
        mature_tree.add_subtree(multi_player)
        not_mature_tree.add_subtree(single_player)
        not_mature_tree.add_subtree(multi_player)

        gen.add_subtree(mature_tree)
        gen.add_subtree(not_mature_tree)
        treee.add_subtree(gen)

    # Adds games to the treee
    for game in games:
        if game.mature:  # the game is mature
            if game.single_player:
                for genre in game.genres:
                    destination = treee.get_subtrees()[genre].get_subtrees()['Mature'].get_subtrees()['Single-Player']
                    destination.add_subtree(tree.GameTree(game))
            else:  # The game is multiplayer
                for genre in game.genres:
                    destination = treee.get_subtrees()[genre].get_subtrees()['Mature'].get_subtrees()['Multi-Player']
                    destination.add_subtree(tree.GameTree(game))
        else:  # The game is not mature
            if game.single_player:
                for genre in game.genres:
                    destination = treee.get_subtrees()[genre].get_subtrees()['Not Mature'].get_subtrees()[
                        'Single-Player']
                    destination.add_subtree(tree.GameTree(game))
            else:  # The game is multiplayer
                for genre in game.genres:
                    destination = treee.get_subtrees()[genre].get_subtrees()['Not Mature'].get_subtrees()['Multi-Player']
                    destination.add_subtree(tree.GameTree(game))
    return treee


def make_suggestions(treee: tree.GameTree, mature: bool, preference: str, genres: list[str],
                     reviews_matter: bool, achievements: bool, budget: float, release_year: int) -> list[str]:
    """
    Return a list of suggestions for the user to play next.

    Preconditions:
    - single_player or multiplayer
    - preference == 'Single player' or preference == 'Multiplayer'
    - budget >= 0
    - release_year >= 1950
    """
    games = []
    subtrees = []
    good_choices_list = []
    for genre in genres:
        if mature:
            if preference == 'Single player':
                destination = treee.get_subtrees()[genre].get_subtrees()['Mature'].get_subtrees()['Single-Player']
                subtrees.append(destination)
            else:  # multiplayer
                destination = treee.get_subtrees()[genre].get_subtrees()['Mature'].get_subtrees()['Multi-Player']
                subtrees.append(destination)
        else:
            if preference == "Single player":
                destination = treee.get_subtrees()[genre].get_subtrees()['Not Mature'].get_subtrees()['Single-Player']
                subtrees.append(destination)
            else:  # multiplayer
                destination = treee.get_subtrees()[genre].get_subtrees()['Not Mature'].get_subtrees()['Multi-Player']
                subtrees.append(destination)
        # destination leads to all the games we can now choose from. Destination is a tree

    # The following chunk filters the list of games based on the user's preferences, like achievements and budget.
    for subtree in subtrees:
        good_choices = []
        for choice in subtree.get_subtrees().values():
            game = choice.node
            if game.price <= budget and game.year >= release_year and (not achievements or game.achievements):
                good_choices.append(game)
        good_choices_list.append(good_choices)

    for games_list in good_choices_list:
        for game in games_list:
            if game not in games:
                games.append(game)

    # good_choices.sort(key=lambda x: x.rating, reverse=True)  # sorts the games by rating

    if reviews_matter:  # The user wants to see the games with the best reviews.
        games.sort(key=lambda x: x.rating, reverse=True)  # sorts the games by rating
    else:
        random.shuffle(games)

    return games


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
        'extra-imports': ['tree', 'random'],
        'disable': ['unused-import', 'too-many-nested-blocks', 'too-many-arguments',
                    'too-many-locals', 'too-many-branches', 'line-too-long']
    })
