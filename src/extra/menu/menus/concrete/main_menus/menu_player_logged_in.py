from extra.menu.menus.abstract.main_menu import MainMenu
from extra.view.view import View


class MenuPlayerLoggedIn(MainMenu):

    def __init__(self):
        super().__init__("Log out", "Play", "Ranking", "Challenges", "Delete account", "Exit")

    # Overridden
    def display(self):
        from main import get_player_logged_in
        from extra.menu.menu_factories.concrete.other.menu_play_factory import MenuPlayFactory
        from extra.menu.menu_factories.concrete.other.menu_ranking_factory import MenuRankingFactory
        from extra.menu.menu_factories.concrete.other.menu_challenge_factory import MenuChallengeFactory
        view = View()
        player_logged_in = get_player_logged_in()
        view.msg("Main Menu")
        for option in range(len(self.options)):
            print(f"({option + 1}) - {self.options[option]}")
        view.row()
        opt = input(f"What do you want to do, {player_logged_in}? ")
        view.clean_prompt()
        if opt not in ["1", "2", "3", "4", "5", "6"]:
            view.msg("Choose a valid option")
        elif opt == "1":
            logged_out = self._log_out()
            if logged_out:
                return  # We need the menu for when a player has logged out (traditional menu)
        elif opt == "2":
            MenuPlayFactory.create_menu().display()
        elif opt == "3":
            MenuRankingFactory.create_menu().display()
        elif opt == "4":
            MenuChallengeFactory.create_menu().display()
        elif opt == "5":
            deleted = self._delete_account(player_logged_in)
            if deleted:
                return
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

    @staticmethod
    def _delete_account(player_nickname: str) -> bool:
        from extra.data_persistence.database_manager import DatabaseManager
        db = DatabaseManager()
        player = db.select_player(player_nickname)
        view = View()
        view.msg("Super Danger Zone")
        print("To enter into this area, we need to check")
        print("whether it is you or not, so type your password")
        view.row()
        password = input("Password: ")
        view.clean_prompt()
        if password.isspace() or len(password) == 0 or password != player.password:
            view.msg("It seems you are not the owner of this account")
            return False
        else:
            view.msg("-> You are about to confirm something impossible to be undone once performed <-",
                     show_lower_line=False)
            view.msg("Are you sure [y/n]? ")
            resp = input("-> ")[0].lower()
            view.clean_prompt()
            if resp == "y":
                from main import set_player_logged_in
                view.msg("Deleting all data from database...")
                view.stop(3)
                db.delete_record("players", {"nickname": player.nickname})
                db.delete_record("challenges", {"receiver_nickname": player.nickname})
                db.delete_record("challenges", {"sender_nickname": player.nickname})
                set_player_logged_in("None")
                view.clean_prompt()
                view.msg("We are sorry for every inconvenience. Thank you for playing our game!")
                input("Press any key to get back: ")
                view.clean_prompt()
                return True
            else:
                view.msg("Canceled")
                return False
