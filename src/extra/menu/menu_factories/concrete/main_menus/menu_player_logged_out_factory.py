from extra.menu.menu_factories.abstract.menu_factory import MenuFactory


class MenuPlayerLoggedOutFactory(MenuFactory):
    from extra.menu.menus.abstract.menu import Menu

    @classmethod
    def create_menu(cls) -> Menu:
        from extra.menu.menus.concrete.main_menus.menu_player_logged_out import MenuPlayerLoggedOut
        if cls.get_menu_obj() is None:
            cls.set_menu_obj(MenuPlayerLoggedOut())
        return cls.get_menu_obj()
