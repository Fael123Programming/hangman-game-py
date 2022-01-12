from extra.menu.menus.menu import Menu


class MenuAccountCreation(Menu):

    def __init__(self):
        super().__init__("Set Nickname", "Set Password", "Main Menu")

    # Overridden
    def display(self):
        pass

    @staticmethod
    def get_out():
        return
