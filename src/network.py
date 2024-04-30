"""CSC111 Winter 2023 Group Project: PlayPal

Instructions
===============================

This Python module contains the CSV reader for the dataset used in this project.


Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of the
Department of Computer Science at the University of Toronto St. George campus.
All forms ofvdistribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for any code we have written
for CSC111, please consult the Course Syllabus.

This file is Copyright (c) 2023 Levent Ozay, Ivan Kraskov.
"""

import csv
import tree


def read_steam_data(steam_data: str) -> dict:
    """Loads the data from the CSV file and returns a dictionary

    The dictionary returned has two key values
        - Games: A list of GameNode objects
        - Genres: A set of strings that represent unique game genres

    Preconditions:
        - steam_data refers to a valid CSV file in the format described on the assignment handout
    """
    with open(steam_data, encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        main_dict = {}
        genres = set()
        games = []
        for row in reader:
            if row[1] == 'app':
                game_genres = row[13].split(",")
                for genre in game_genres:
                    genres.add(genre)
                game_name = get_game_name(row[2])
                rating = get_game_review(row[5])
                mature = get_mature_content(row[15])
                achievements = get_achievements(row[12])
                price = get_price(row[18])
                single = get_single_player(row[10])
                multi = get_multi_player(row[10])
                age = get_release_year(row[6])
                game = tree.GameNode(game_genres, game_name, rating, mature, achievements,
                                     row[16], row[17], price, single, multi, age)
                games.append(game)
        main_dict['Genres'] = genres
        main_dict['Games'] = games
        return main_dict


def get_game_name(game_name: str) -> str:
    """A helper function for read_steam_data that helps get names of games that
    cannot be encoded using the default encoder (UTF-8)

    Preconditions:
    - isinstance(game_name, str)
    """
    try:
        encoded_name = game_name.encode('utf-8')
    except UnicodeEncodeError:
        return ''
    return encoded_name.decode('utf-8')


def get_game_review(review_str: str) -> int:
    """A helper function for read_steam_data that helps get the rating percentage
     of the game from its given review string

    Preconditions:
    - isinstance(review_str, str)
    """
    if '%' in review_str:
        percentage_index = review_str.find('%')
        if review_str[percentage_index - 3] == '1' and review_str[percentage_index - 2] == '0':  # if rating 100
            return 100
        elif review_str[percentage_index - 2] == ' ':  # if rating between 0-9 inclusive
            return int(review_str[percentage_index - 1:percentage_index])
        else:
            return int(review_str[percentage_index - 2:percentage_index])
    else:
        return 0


def get_mature_content(mature_str: str) -> bool:
    """A helper function for read_steam_data that helps get whether a game has
    mature content or not

    Preconditions:
    - isinstance(mature_str, str)
    """
    if mature_str in {'', 'NaN'}:
        return False
    else:
        return True


def get_achievements(achievement_str: str) -> bool:
    """A helper function for read_steam_data that helps get whether a game has
    achievements or not

    Preconditions:
    - isinstance(achievement_str, str)
    """
    if achievement_str == 'NaN':
        return False
    else:
        return True


def get_price(price_str: str) -> float:
    """A helper function for read_steam_data that helps get the price of a game
    in USD

    Preconditions:
    - isinstance(price_str, str)
    """
    if '$' in price_str:
        return float(price_str[1:])
    else:
        return 0


def get_single_player(game_details: str) -> bool:
    """A helper function for read_steam_data that helps get whether the game is
    single-player or not

    Preconditions:
    - isinstance(game_details, str)
    """
    if 'Single-player' in game_details:
        return True
    else:
        return False


def get_multi_player(game_details: str) -> bool:
    """A helper function for read_steam_data that helps get whether the game is
    multiplayer or not

    Preconditions:
    - isinstance(game_details, str)
    """
    if 'Multi-player' in game_details:
        return True
    else:
        return False


def get_release_year(game_details: str) -> int:
    """A helper function for read_steam_data that helps get the release year of the game

    Return 0 if the game has no release year specified

    Preconditions:
    - isinstance(game_details, str)
    """
    if ',' in game_details:
        index = game_details.find(', ')
        try:
            age = int(game_details[index + 1:])
        except ValueError:
            return 0
        return age

    return 0


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
        'extra-imports': ['tree', 'csv'],
        'disable': ['unused-import', 'too-many-locals', 'forbidden-IO-function']
    })
