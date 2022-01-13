from extra.menu.menus.main_menu import MainMenu
from extra.view.view import View
from extra.player.player import Player


class MenuPlayerLoggedIn(MainMenu):

    def __init__(self):
        super().__init__("Log out", "Play", "Ranking", "Delete Account", "Exit")

    # Overridden
    def display(self):
        from main import get_player_logged_in
        view = View()
        player_logged_in = get_player_logged_in()
        view.msg("Main Menu", 150)
        for option in range(len(self.options)):
            print(f"({option + 1}) - {self.options[option]}")
        view.row(150)
        opt = input(f"What do you want to do, {player_logged_in}? ")
        view.clean_prompt()
        if opt not in ["1", "2", "3", "4", "5"]:
            view.msg("Choose a valid option", 150)
        elif opt == "1":
            logged_out = self._log_out()
            if logged_out:
                return
        elif opt == "2":
            view.msg("Play a game", 150)
        elif opt == "3":
            view.msg("Ranking", 150)
        elif opt == "4":
            view.msg("Delete account", 150)
        else:
            self.get_out()
        view.stop(1)
        view.clean_prompt()

    @staticmethod
    def _log_out() -> bool:
        from main import set_player_logged_in
        view = View()
        view.msg("Are you sure? [y/n]", 150)
        if input("-> ")[0].lower() == "y":
            view.clean_prompt()
            view.msg("Getting out...", 150)
            view.stop(1)
            view.clean_prompt()
            set_player_logged_in("None")
            return True
        return False
