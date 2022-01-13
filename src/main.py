from extra.menu.menu_factories.menu_player_logged_in_factory import MenuPlayerLoggedInFactory
from extra.menu.menu_factories.menu_player_logged_out_factory import MenuPlayerLoggedOutFactory
from sys import path
import os


def is_a_player_logged_in():
    return get_player_logged_in() != "None"


def get_proper_menu():
    if is_a_player_logged_in():
        return MenuPlayerLoggedInFactory.create_menu()
    return MenuPlayerLoggedOutFactory.create_menu()


def create_file_player_logged_in(file_path: str):
    if not os.path.isfile(file_path):
        with open(file_path, "x"):
            pass


def set_player_logged_in(player_nickname):
    global player_logged_in_file
    try:
        with open(player_logged_in_file, "wt") as file:
            file.write(player_nickname)
    except FileNotFoundError:
        print("Before setting the current player logged in, create a file to record it")
        print("So it can be visible by other classes of this project")
        print("Use create_file_player_logged_in(file_path)")


def get_player_logged_in():
    global player_logged_in_file
    try:
        with open(player_logged_in_file, "rt") as file:
            return file.readline()
    except FileNotFoundError:
        print("Before getting the current player logged in, create a file to record it")
        print("So it can be visible by other classes of this project")
        print("Use create_file_player_logged_in(file_path)")


def del_player_logged_in_file():
    global player_logged_in_file
    try:
        os.remove(player_logged_in_file)
    except FileNotFoundError:
        print("Cannot remove a nonexistent file")
        

player_logged_in_file = path[1] + "/extra/data_persistence/player_logged_in.txt"

if __name__ == "__main__":
    create_file_player_logged_in(player_logged_in_file)
    set_player_logged_in("None")
    # View().load("Welcome to Hangman Game", 150)
    while True:
        menu = get_proper_menu()
        # If there is no user logged in or there is a user logged in, then returns a menu for either case.
        menu.display()

