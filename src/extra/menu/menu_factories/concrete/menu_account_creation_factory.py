from extra.menu.menu_factories.abstract.menu_factory import MenuFactory


class MenuAccountCreationFactory(MenuFactory):
    from extra.menu.menus.abstract.menu import Menu

    @classmethod
    def create_menu(cls) -> Menu:
        from extra.menu.menus.concrete.menu_account_creation import MenuAccountCreation
        if cls.get_menu_obj() is None:
            cls.set_menu_obj(MenuAccountCreation())
        return cls.get_menu_obj()
