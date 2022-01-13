from extra.menu.menus.main_menu import MainMenu


class MenuPlayerLoggedIn(MainMenu):

    def __init__(self):
        super().__init__("Log out", "Play", "Ranking", "Delete Account", "Exit")

    # Overridden
    def display(self):
        from main import get_player_logged_in
        from extra.view.view import View
        view = View()
        player_logged_in = get_player_logged_in()
        view.msg("Main Menu")
        for option in range(len(self.options)):
            print(f"({option + 1}) - {self.options[option]}")
        view.row()
        opt = input(f"What do you want to do, {player_logged_in}? ")
        view.clean_prompt()
        if opt not in ["1", "2", "3", "4", "5"]:
            view.msg("Choose a valid option")
        elif opt == "1":
            logged_out = self._log_out()
            if logged_out:
                return
        elif opt == "2":
            view.msg("Play a game")
        elif opt == "3":
            view.msg("Ranking")
        elif opt == "4":
            view.msg("Delete account")
        else:
            self.get_out()
        view.stop()
        view.clean_prompt()

    @staticmethod
    def _log_out() -> bool:
        from main import set_player_logged_in
        from extra.view.view import View
        view = View()
        view.msg("Are you sure? [y/n]")
        if input("-> ")[0].lower() == "y":
            view.clean_prompt()
            view.msg("Getting out...")
            view.stop()
            view.clean_prompt()
            set_player_logged_in("None")
            return True
        return False
