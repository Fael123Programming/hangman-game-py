from extra.menu.menu_factories.menu_factory import MenuFactory
from extra.menu.menus.menu import Menu
from extra.menu.menus.menu_account_creation import MenuAccountCreation


class MenuAccountCreationFactory(MenuFactory):

    @classmethod
    def create_menu(cls) -> Menu:
        if cls.get_menu_obj() is None:
            cls.set_menu_obj(MenuAccountCreation())
        return cls.get_menu_obj()
