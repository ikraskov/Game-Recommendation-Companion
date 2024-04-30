"""CSC111 Winter 2023 Group Project: PlayPal

Instructions
===============================

This Python module contains the main function that runs PlayPal

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of the
Department of Computer Science at the University of Toronto St. George campus.
All forms ofvdistribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for any code we have written
for CSC111, please consult the Course Syllabus.

This file is Copyright (c) 2023 Levent Ozay, Ivan Kraskov.
"""

import network
import tree_generator
import tkinter_start


def main():
    """
    The main function for the PlayPal program.
    """
    main_file = network.read_steam_data('steam_games.csv')
    tree = tree_generator.load_game_tree(main_file)
    tkinter_start.main_method(tree)


if __name__ == '__main__':
    main()
