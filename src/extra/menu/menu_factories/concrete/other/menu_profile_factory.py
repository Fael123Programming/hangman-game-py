from extra.menu.menu_factories.abstract.menu_factory import MenuFactory


class MenuProfileFactory(MenuFactory):
    from extra.menu.menus.abstract.menu import Menu

    @classmethod
    def create_menu(cls) -> Menu:
        from extra.menu.menus.concrete.other.menu_profile import MenuProfile
        if cls.get_menu_obj() is None:
            cls.set_menu_obj(MenuProfile())
        return cls.get_menu_obj()
