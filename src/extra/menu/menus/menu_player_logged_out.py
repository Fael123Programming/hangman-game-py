from extra.menu.menus.main_menu import MainMenu


class MenuPlayerLoggedOut(MainMenu):

    def __init__(self):
        super().__init__("Log in", "Sign Up", "Just Play", "Exit")

    # Overridden
    def display(self):
        from extra.view.view import View
        from extra.menu.menu_factories.menu_play_factory import MenuPlayFactory
        from extra.menu.menu_factories.menu_account_creation_factory import MenuAccountCreationFactory
        view = View()
        view.msg("Main Menu", 150)
        for option in range(len(self.options)):
            print(f"({option + 1}) - {self.options[option]}")
        view.row()
        opt = input("What do you want to do? ")
        view.clean_prompt()
        if opt not in ["1", "2", "3", "4"]:
            view.msg("Choose a valid option")
            view.stop()
        elif opt == "1":
            logged_in = self._log_in()
            if logged_in:
                return
        elif opt == "2":
            MenuAccountCreationFactory.create_menu().display()
        elif opt == "3":
            MenuPlayFactory.create_menu().display()
        elif opt == "4":
            self.get_out()
        view.clean_prompt()

    @staticmethod
    def _log_in():
        from extra.view.view import View
        from extra.data_persistence.database_manager import DataBaseManager
        view = View()
        view.msg("Log into your account")
        nickname = input("Nickname: ")
        if nickname.isspace() or len(nickname) == 0:
            view.clean_prompt()
            view.msg("Invalid nickname")
            view.stop()
            return False
        password = input("Password: ")
        if password.isspace() or len(password) == 0:
            view.clean_prompt()
            view.msg("Invalid password")
            view.stop()
            return False
        view.clean_prompt()
        view.msg("Checking database...")
        view.stop()
        view.clean_prompt()
        player = DataBaseManager("database").select_player(nickname)
        if player is None:
            view.msg(f"Player {nickname} does not exist")
            view.stop()
            return False
        elif player.password != password:
            view.msg("Invalid password")
            view.stop()
            return False
        else:
            from main import set_player_logged_in
            set_player_logged_in(player.nickname)
            return True
