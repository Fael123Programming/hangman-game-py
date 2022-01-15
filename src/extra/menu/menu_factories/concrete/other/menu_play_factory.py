from extra.menu.menu_factories.abstract.menu_factory import MenuFactory


class MenuPlayFactory(MenuFactory):
    from extra.menu.menus.abstract.menu import Menu

    @classmethod
    def create_menu(cls) -> Menu:
        from extra.menu.menus.concrete.other.menu_play import MenuPlay
        if cls.get_menu_obj() is None:
            cls.set_menu_obj(MenuPlay())
        return cls.get_menu_obj()
