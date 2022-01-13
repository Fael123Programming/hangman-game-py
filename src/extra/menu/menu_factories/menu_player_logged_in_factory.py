from extra.menu.menu_factories.menu_factory import MenuFactory
from extra.menu.menus.menu_player_logged_in import MenuPlayerLoggedIn


class MenuPlayerLoggedInFactory(MenuFactory):

    @classmethod
    def create_menu(cls):
        if cls.get_menu_obj() is None:
            cls.set_menu_obj(MenuPlayerLoggedIn())
        return cls.get_menu_obj()
