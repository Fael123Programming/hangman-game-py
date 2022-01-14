from extra.menu.menu_factories.abstract.menu_factory import MenuFactory


class MenuPlayerLoggedInFactory(MenuFactory):
    from extra.menu.menus.abstract.menu import Menu

    @classmethod
    def create_menu(cls) -> Menu:
        from extra.menu.menus.concrete.menu_player_logged_in import MenuPlayerLoggedIn
        if cls.get_menu_obj() is None:
            cls.set_menu_obj(MenuPlayerLoggedIn())
        return cls.get_menu_obj()
