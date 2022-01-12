from extra.menu.menu_factories.menu_player_logged_in_factory import MenuPlayerLoggedInFactory
from extra.menu.menu_factories.menu_player_logged_out_factory import MenuPlayerLoggedOutFactory
from sys import path
from extra.view.view import View


def is_a_player_logged_in():
    return player_logged_in is not None


def get_proper_menu():
    if is_a_player_logged_in():
        return MenuPlayerLoggedInFactory().create_menu()
    return MenuPlayerLoggedOutFactory().create_menu()


def set_player_logged_in(str_player: str):
    try:
        with open(player_logged_in_file, "x") as file:
            file.write(str_player)
    except FileExistsError:
        pass  # No problems for that


def get_player_logged_in():
    global player_logged_in_file
    try:
        with open(player_logged_in_file, "rt") as file:
            return file.readline()
    except FileNotFoundError:
        print("Not file found at " + player_logged_in_file)


def del_player_logged_in_file():
    import os
    try:
        os.remove(player_logged_in_file)
    except FileNotFoundError:
        print("Cannot remove a nonexistent file")
        

player_logged_in_file = path[1] + "/extra/data_persistence/player_logged_in.txt"
player_logged_in = None

set_player_logged_in("None")

if __name__ == "__main__":
    View().load("Welcome to Hangman Game", 150)
    while True:
        menu = get_proper_menu()
        # If there is no user logged in or there is a user logged in, then returns a menu for either case.
        menu.display()

