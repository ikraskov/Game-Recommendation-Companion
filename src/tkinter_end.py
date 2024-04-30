"""CSC111 Winter 2023 Project: PlayPal

This module creates an interactive game list viewer using the tkinter library.
The main_method function takes a list of GameNode instances as input and
creates a window to display their information. The user can navigate through
the list of games using previous and next buttons. The current game's information
is displayed in a label, and the display_game function is called each time the user
navigates to a new game. The viewer also includes information such as the game's
name, genres, rating, maturity level, achievements, system requirements, price,
single and multiplayer modes, and release year. The module uses global variables
to keep track of the current index in the list of games and the maximum index,
and includes error checking to prevent navigating beyond the bounds of the list.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of the
Department of Computer Science at the University of Toronto St. George campus.
All forms ofvdistribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for any code we have written
for CSC111, please consult the Course Syllabus.


This file is Copyright (c) 2023 Levent Ozay, Ivan Kraskov.
"""
import tkinter as tk


def main_method(games: list) -> None:
    """
    This function creates an interactive game list viewer using the tkinter library.
    It takes a list of GameNode instances as input and assumes that each element of
    the list is an instance of the GameNode class.

    Preconditions:

    - games != []
    - all(isinstance(game, GameNode) for game in games)

    Representation Invariants:

    The GameNode class must have the following attributes:
    - name (str): the name of the game.
    - genres (list): a list of strings representing the genres of the game.
    - rating (float): a float representing the rating of the game.
    - mature (bool): a boolean value indicating whether the game is mature or not.
    - achievements (int): an integer representing the number of achievements in the game.
    - min_req (str): a string representing the minimum system requirements for the game.
    - rec_req (str): a string representing the recommended system requirements for the game.
    - price (float): a float representing the price of the game.
    - single_player (bool): a boolean value indicating whether the game has a single-player mode or not.
    - multi_player (bool): a boolean value indicating whether the game has a multiplayer mode or not.
    - year (int): an integer representing the release year of the game.
    """
    current_index = 0
    # Create a Tkinter window
    window = tk.Tk()
    window.title('PlayPal Games List')

    # Check if the input list is empty
    if not games:
        game_info = tk.Label(window, font=("Arial", 12),
                             text="Sorry, there are no games that match your input, please try again.")
        game_info.pack(pady=20)
        return

    # Create a list of GameNode instances
    game_list = games

    # Define variables for keeping track of the current index in the game list
    max_index = len(game_list) - 1

    # Define a function to display the current GameNode
    def display_game() -> None:
        """
        The display_game method updates a label in a Tkinter window to display the current
        GameNode object in the game_list list based on the current_index variable.

        Preconditions:

        - game_list != [] and all(isinstance(game, GameNode) for game in game_list)
        - 0 < current_index < len(game_list)
        """
        current_game = game_list[current_index]
        game_info.config(text=f"Name: {current_game.name}\n"
                              f"Genres: {current_game.genres}\n"
                              f"Rating: {current_game.rating}\n"
                              f"Mature: {current_game.mature}\n"
                              f"Achievements: {current_game.achievements}\n"
                              f"Minimum requirements: {current_game.min_req}\n"
                              f"Recommended requirements: {current_game.rec_req}\n"
                              f"Price: ${current_game.price}\n"
                              f"Single player: {current_game.single_player}\n"
                              f"Multi player: {current_game.multi_player}\n"
                              f"Year: {current_game.year}")

    # Create a label for displaying game information
    game_info = tk.Label(window, font=("Arial", 12))
    game_info.pack(pady=20)

    # Create a previous button
    def prev_game() -> None:
        """
        Decrements the current index by 1 and displays the previous game in the game list if it exists.

        Preconditions:
        - 0 < current_index
        """
        nonlocal current_index
        if current_index > 0:
            current_index -= 1
            display_game()

    prev_button = tk.Button(window, text='Previous', command=prev_game)
    prev_button.pack(side='left', padx=20)

    # Create a next button
    def next_game() -> None:
        """
        Displays the next game in the game list.

        Preconditions:
        - 0 < current_index
        - max_index == len(game_list) - 1
        """
        nonlocal current_index
        if current_index < max_index:
            current_index += 1
            display_game()

    next_button = tk.Button(window, text='Next', command=next_game)
    next_button.pack(side='right', padx=20)

    # Display the first game
    display_game()

    # Start the main loop
    window.mainloop()


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
        'extra-imports': ['tkinter'],
        'disable': ['unused-import', 'forbidden']
    })
