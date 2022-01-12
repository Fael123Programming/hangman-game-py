from extra.menu.menu_factories.menu_factory import MenuFactory
from extra.menu.menus.menu_account_creation import MenuAccountCreation


class MenuAccountCreationFactory(MenuFactory):

    def __init__(self):
        super().__init__()

    # Overridden
    def create_menu(self):
        if self._menu_obj is None:
            self._menu_obj = MenuAccountCreation()
        return self._menu_obj
