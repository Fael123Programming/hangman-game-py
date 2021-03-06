from abc import ABC
from extra.menu.menus.abstract.menu import Menu


class MainMenu(Menu, ABC):

    @staticmethod
    def get_out():
        from sys import exit
        from extra.view.view import View
        view = View()
        view.msg("Are you sure? [y/n]")
        if input("-> ")[0].lower() == "y":
            from main import del_player_logged_in_file
            view.clean_prompt()
            view.msg("Goodbye!")
            view.stop()
            view.clean_prompt()
            del_player_logged_in_file()
            exit()  # Shuts PVM down.
        view.clean_prompt()
