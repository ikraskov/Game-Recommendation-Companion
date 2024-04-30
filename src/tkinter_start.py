"""CSC111 Winter 2023 Project: PlayPal

A GUI interface for PlayPal, a game recommendation system.
The user is presented with a series of questions to gather their game preferences,
such as preferred play mode, budget, genres, release year, reviews, achievements, and mature content.
Based on the user's choices, the system generates a list of game suggestions using the provided GameTree
object and displays them in another GUI using the tkinter_end module.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of the
Department of Computer Science at the University of Toronto St. George campus.
All forms ofvdistribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for any code we have written
for CSC111, please consult the Course Syllabus.

This file is Copyright (c) 2023 Levent Ozay, Ivan Kraskov
"""
import tkinter as tk
import tree
import tree_generator
import tkinter_end


def main_method(treee: tree.GameTree) -> None:
    """
    A function that displays a GUI interface to gather user preferences for a video game.

    Preconditions:
    - treee is GameTree()
    """
    root = tk.Tk()
    root.title('PlayPal')

    # function to get user's choices
    def submit() -> None:
        """
        A function that retrieves the user's preferences from the GUI interface and generates video game suggestions
        based on these preferences. The suggestions are displayed using the tkinter_end.main_method method.

        Preconditions:
        - var_play_mode is a tkinter.StringVar with value 'Single player' or 'Multiplayer'
        - var_budget is a tkinter.StringVar with value in format '$[float]'
        - var_genres is a dictionary containing tkinter.IntVar values as its values
        - var_year is a tkinter.StringVar with value in format '[int]'
        - var_reviews is a tkinter.BooleanVar with value True or False
        - var_achievements is a tkinter.BooleanVar with value True or False
        - var_mature_content is a tkinter.BooleanVar with value True or False
        - treee is an instance of the GameTree class
        """
        player = var_play_mode.get()  # Multiplayer, Single player
        budget = float(var_budget.get()[1:])
        genress = [genree for genree, varr in var_genres.items() if varr.get()]
        release_year = int(var_year.get())
        reviews_matter = var_reviews.get()
        achievements = var_achievements.get()
        mature = var_mature_content.get()
        if len(genress) == 0:  # if the user didn't pick any genres, we'll give use all of them
            genress = ['Action', 'Design & Illustration', 'Movie', 'Early Access',
                       'Casual', 'Animation & Modeling', 'Web Publishing', 'Photo Editing',
                       'Education', 'Valve', 'Strategy', 'Game Development', 'Audio Production',
                       'Sports', 'Software Training', 'Massively Multiplayer', 'Free to Play',
                       'Adventure', 'Video Production', 'Racing', 'Accounting', 'RPG', 'Indie',
                       'Simulation', 'Utilities']
        games = tree_generator.make_suggestions(treee, mature, player, genress, reviews_matter, achievements, budget,
                                                release_year)
        tkinter_end.main_method(games)

    # add image to the top-left corner
    photo = tk.PhotoImage(file='My_project.png')
    label = tk.Label(root, image=photo)
    label.pack(side='top', anchor='n')

    # play mode question
    tk.Label(root, text='Which do you prefer playing?').pack()
    var_play_mode = tk.StringVar(value='Single player')  # default value
    tk.Radiobutton(root, text='Single player', variable=var_play_mode, value='Single player').pack()
    tk.Radiobutton(root, text='Multiplayer', variable=var_play_mode, value='Multiplayer').pack()

    # budget question
    tk.Label(root, text='What\'s your maximum budget?').pack()
    var_budget = tk.StringVar(value='$0')  # default value
    tk.Entry(root, textvariable=var_budget).pack()

    # genres question
    tk.Label(root, text='What are some genres that you enjoy most? (Pick empty box for all genres)').pack()

    # Create a frame to contain the checkboxes
    genres_frame = tk.Frame(root)
    genres_frame.pack()

    var_genres = {}
    genres = ['', 'Action', 'Design & Illustration', 'Movie', 'Early Access',
              'Casual', 'Animation & Modeling', 'Web Publishing', 'Photo Editing',
              'Education', 'Valve', 'Strategy', 'Game Development', 'Audio Production',
              'Sports', 'Software Training', 'Massively Multiplayer', 'Free to Play',
              'Adventure', 'Video Production', 'Racing', 'Accounting', 'RPG', 'Indie',
              'Simulation', 'Utilities', 'HTC']

    # Calculate the number of columns needed
    num_cols = 5

    # Create the checkboxes in the frame
    for i, genre in enumerate(genres):
        var = tk.IntVar()
        var_genres[genre] = var
        checkbox = tk.Checkbutton(genres_frame, text=genre, variable=var)
        row, col = divmod(i, num_cols)
        checkbox.grid(row=row, column=col, sticky="w")

    # release year question
    tk.Label(root,
             text='What is the oldest date of release you\'d allow? (Note: old games are still fantastic!)').pack()
    var_year = tk.StringVar(value='0')  # default value
    tk.Entry(root, textvariable=var_year).pack()

    # reviews question
    tk.Label(root, text='Are the game\'s reviews important to you?').pack()
    var_reviews = tk.BooleanVar(value=True)  # default value
    tk.Radiobutton(root, text='Yes', variable=var_reviews, value=True).pack()
    tk.Radiobutton(root, text='No', variable=var_reviews, value=False).pack()

    # achievements question
    tk.Label(root, text='Do achievements matter to you?').pack()
    var_achievements = tk.BooleanVar(value=True)  # default value
    tk.Radiobutton(root, text='Yes', variable=var_achievements, value=True).pack()
    tk.Radiobutton(root, text='No', variable=var_achievements, value=False).pack()

    # mature content question
    tk.Label(root, text='Are you comfortable with mature content in games?').pack()
    var_mature_content = tk.BooleanVar(value=True)  # default value
    tk.Radiobutton(root, text='Yes', variable=var_mature_content, value=True).pack()
    tk.Radiobutton(root, text='No', variable=var_mature_content, value=False).pack()

    # submit button
    tk.Button(root, text='Submit', command=submit).pack()

    root.mainloop()


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
        'extra-imports': ['tree_generator', 'tkinter_end', 'tkinter', 'tree'],
        'disable': ['unused-import', 'too-many-locals', 'too-many-statements']
    })
