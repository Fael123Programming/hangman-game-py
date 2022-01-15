from extra.menu.menu_factories.abstract.menu_factory import MenuFactory


class MenuChallengeFactory(MenuFactory):

    @classmethod
    def create_menu(cls):
        from extra.menu.menus.concrete.other.menu_challenge import MenuChallenge
        if cls.get_menu_obj() is None:
            cls.set_menu_obj(MenuChallenge())
        return cls.get_menu_obj()
