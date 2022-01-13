from extra.menu.menus.menu import Menu
from extra.view.view import View
from extra.data_persistence.database_manager import DataBaseManager
from extra.player.player import Player


class MenuAccountCreation(Menu):

    def __init__(self):
        super().__init__("Set Nickname", "Set Password", "Create Account", "Main Menu")

    # Overridden
    def display(self):
        view = View()
        nickname = password = None

        def not_valid_credentials():
            return nickname is None or password is None

        while True:
            view.clean_prompt()
            view.msg("Menu Account Creation")
            for option in range(len(self.options)):
                if option == 2 and not_valid_credentials():
                    continue
                if option == 3 and not_valid_credentials():
                    print(f"({option}) - {self.options[option]}")
                else:
                    print(f"({option + 1}) - {self.options[option]}")
            view.row()
            print(f"Nickname: {nickname}")
            print(f"Password: {password}")
            view.row()
            opt = input("What do you want to do? ")
            view.clean_prompt()
            if not_valid_credentials():
                if opt not in ["1", "2", "3"]:
                    view.msg("Choose a valid option")
                elif opt == "1":
                    nickname = self._set_nickname()
                elif opt == "2":
                    password = self._set_password()
                else:
                    return
            else:
                if opt not in ["1", "2", "3", "4"]:
                    view.msg("Choose a valid option")
                elif opt == "1":
                    nickname = self._set_nickname()
                elif opt == "2":
                    password = self._set_password()
                elif opt == "3":
                    created = self._create_account(nickname, password)
                    if created:
                        return
                else:
                    return
            view.stop()

    @staticmethod
    def _set_nickname():
        view = View()
        view.msg("Set Nickname")
        nickname = input("Type a nickname: ")
        view.clean_prompt()
        if nickname.isspace() or len(nickname) == 0:
            view.msg("Invalid nickname")
            return None
        else:
            view.msg("Checking if it has not already been used...")
            view.stop()
            view.clean_prompt()
            player = DataBaseManager("database").select_player(nickname)
            if player is not None:
                view.msg(f"Unfortunately {nickname} is already taken")
                return None
            else:
                view.msg(f"Great, {nickname} is available!")
                return nickname

    @staticmethod
    def _set_password():
        view = View()
        view.msg("Set Password")
        password = input("Type a password (it would be safer \nif you choose a strong one): ")
        view.clean_prompt()
        if password.isspace() or len(password) == 0:
            view.msg("Invalid password")
            return None
        view.msg(f"Your password is {password} so do not forget it")
        return password

    @staticmethod
    def _create_account(nickname: str, password: str):
        view = View()
        view.msg(f"Nickname: {nickname}", show_upper_line=True, show_lower_line=False)
        view.msg(f"Password: {password}", show_upper_line=False, show_lower_line=False)
        view.msg(f"Are you sure [y/n]? ", show_upper_line=False, show_lower_line=True)
        resp = input("-> ")[0].lower()
        view.clean_prompt()
        if resp == "y":
            player = Player(nickname, password)
            DataBaseManager("database").insert_data("players", player.__str__())
            view.msg("Account created successfully")
            view.stop()
            return True
        view.msg("Canceled")
        return False
