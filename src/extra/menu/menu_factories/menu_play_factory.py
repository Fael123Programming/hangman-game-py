from extra.menu.menu_factories.menu_factory import MenuFactory
from extra.menu.menus.menu_play import MenuPlay


class MenuPlayFactory(MenuFactory):

    @classmethod
    def create_menu(cls):
        if cls.get_menu_obj() is None:
            cls.set_menu_obj(MenuPlay())
        return cls.get_menu_obj()
