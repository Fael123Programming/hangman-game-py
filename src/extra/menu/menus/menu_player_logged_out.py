from extra.menu.menus.menu import Menu
from extra.menu.menus.menu_account_creation import MenuAccountCreation
from extra.view.view import View


class MenuPlayerLoggedOut(Menu):

    def __init__(self):
        super().__init__("Log in", "Sign Up", "Just Play", "Exit")

    # Overridden
    def display(self):
        view = View()
        view.msg("Main Menu", 150)
        for option in range(len(self.options)):
            print(f"({option + 1}) - {self.options[option]}")
        view.row(150)
        opt = input("What do you want to do? ")
        view.clean_prompt()
        if opt not in ["1", "2", "3", "4"]:
            view.msg("Choose a valid option", 150)
            view.stop(1)
        elif opt == "1":
            # If user has logged into their account properly and correctly,
            # this piece of code must change 'player_logged_in' to the right
            # player object and end this method execution by 'return'.
            view.msg("Log into your account", 150)
            view.stop(1)
        elif opt == "2":
            MenuAccountCreation().display()
        elif opt == "3":
            view.msg("Play menu", 150)
            view.stop(1)
        elif opt == "4":
            self.get_out()
        view.clean_prompt()
