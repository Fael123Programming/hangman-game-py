from extra.menu.menus.menu import Menu
from extra.view.view import View
from extra.player.player import Player


class MenuPlayerLoggedIn(Menu):

    def __init__(self):
        super().__init__("Log out", "Play", "Ranking", "Delete Account", "Exit")

    # Overridden
    def display(self):
        view = View()
        view.msg("Main Menu", 150)
        for option in range(len(self.options)):
            print(f"({option + 1}) - {self.options[option]}")
        view.row(150)
        opt = input(f"What do you want to do, {player_logged_in.nickname}? ")
        view.clean_prompt()
        if opt not in ["1", "2", "3", "4", "5"]:
            view.msg("Choose a valid option", 150)
            view.stop(1)
        elif opt == "1":
            view.msg("Are you sure? [y/n]", 150)
            if input("-> ")[0].lower() == "y":
                view.clean_prompt()
                view.msg("Getting out...", 150)
                player_logged_in = None
                view.stop(2)
            view.clean_prompt()
        elif opt == "2":
            view.msg("Play a game", 150)
            view.stop(1)
        elif opt == "3":
            view.msg("Ranking", 150)
            view.stop(1)
        elif opt == "4":
            view.msg("Delete account", 150)
            view.stop(1)
        else:
            self.get_out()
        view.clean_prompt()
