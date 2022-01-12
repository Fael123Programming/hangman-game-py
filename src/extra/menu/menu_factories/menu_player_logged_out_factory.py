from extra.menu.menu_factories.menu_factory import MenuFactory
from extra.menu.menus.menu_player_logged_out import MenuPlayerLoggedOut


class MenuPlayerLoggedOutFactory(MenuFactory):

    def __init__(self):
        super().__init__()

    # Overridden
    def create_menu(self):
        if self._menu_obj is None:
            self._menu_obj = MenuPlayerLoggedOut()
        return self._menu_obj
