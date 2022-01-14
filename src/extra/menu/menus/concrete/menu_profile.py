from extra.menu.menus.abstract.menu import Menu
from extra.view.view import View


class MenuProfile(Menu):
    from extra.player.player import Player

    def __init__(self):
        super().__init__("Info", "Change Nickname", "Change Password", "Ranking")

    def display(self):
        from extra.data_persistence.database_manager import DatabaseManager
        from main import get_player_logged_in
        view = View()
        db = DatabaseManager()
        player = db.select_player(get_player_logged_in())
        while True:
            view.msg("Profile")
            for option in range(len(self.options)):
                print(f"({option + 1}) - {self.options[option]}")
            view.row()
            opt = input(f"What do you want to do, {player.nickname}? ")
            view.clean_prompt()
            if opt not in ["1", "2", "3", "4"]:
                view.msg("Choose a valid option")
            elif opt == "1":
                self._info(player)
            elif opt == "2" or opt == "3":
                view.msg("Danger zone")
                print("To enter into this area, we need to check")
                print("whether it is you or not, so type your password")
                view.row()
                password = input("Password: ")
                view.clean_prompt()
                if password.isspace() or len(password) == 0 or password != player.password:
                    view.msg("It seems you are not the owner of this account")
                elif opt == "2":
                    self._change_nickname(player)
                elif opt == "3":
                    self._change_password(player)
            else:
                return
            view.stop()
            view.clean_prompt()

    @staticmethod
    def _info(player: Player):
        view = View()
        view.msg("Profile Information")
        print(f"Player nickname: {player.nickname}")
        view.row()
        print(f"Matches played: {player.performance.matches_played}")
        print(f"Match victories: {player.performance.match_victories}")
        print(f"Match defeats: {player.performance.match_defeats}")
        view.row()
        print(f"Challenges played: {player.performance.challenges_played}")
        print(f"Challenge victories: {player.performance.challenge_victories}")
        print(f"Challenge defeats: {player.performance.challenge_defeats}")
        print(f"Challenges made: {player.performance.challenges_made}")
        view.row()
        print(f"Yield coefficient: {player.performance.yield_coefficient}")
        view.row()
        input("Press any key to get back: ")
        view.clean_prompt()

    @staticmethod
    def _change_nickname(player: Player):
        from extra.menu.menus.concrete.menu_account_creation import MenuAccountCreation
        from extra.data_persistence.database_manager import DatabaseManager
        new_nickname = MenuAccountCreation.set_nickname()
        view = View()
        db = DatabaseManager()
        view.stop()
        if new_nickname is not None:
            view.msg("Are you sure [y/n]?", show_upper_line=False)
            resp = input("-> ")[0].lower()
            view.clean_prompt()
            if resp == "y":
                from main import set_player_logged_in
                db.update_record("players", {"nickname": new_nickname}, {"nickname": player.nickname})
                player.nickname = new_nickname
                set_player_logged_in(player.nickname)
                view.msg("Nickname changed successfully")
            else:
                view.msg("Canceled")

    @staticmethod
    def _change_password(player: Player):
        from extra.menu.menus.concrete.menu_account_creation import MenuAccountCreation
        from extra.view.view import View
        from extra.data_persistence.database_manager import DatabaseManager
        view = View()
        db = DatabaseManager()
        new_password = MenuAccountCreation.set_password()
        view.stop()
        if new_password is not None:
            view.msg("Are you sure [y/n]?", show_upper_line=False)
            resp = input("-> ")[0].lower()
            view.clean_prompt()
            if resp == "y":
                db.update_record("players", {"password": new_password}, {"nickname": player.nickname})
                player.password = new_password
                view.msg("Password changed successfully")
            else:
                view.msg("Canceled")
