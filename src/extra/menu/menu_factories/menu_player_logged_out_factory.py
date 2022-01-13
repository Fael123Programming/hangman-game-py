from extra.menu.menu_factories.menu_factory import MenuFactory
from extra.menu.menus.menu_player_logged_out import MenuPlayerLoggedOut


class MenuPlayerLoggedOutFactory(MenuFactory):

    @classmethod
    def create_menu(cls):
        if cls.get_menu_obj() is None:
            cls.set_menu_obj(MenuPlayerLoggedOut())
        return cls.get_menu_obj()
