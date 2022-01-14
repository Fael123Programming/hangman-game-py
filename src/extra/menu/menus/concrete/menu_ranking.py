from extra.menu.menus.abstract.menu import Menu


class MenuRanking(Menu):

    def __init__(self):
        super().__init__("Profile", "Global Rank", "Main Menu")

    def display(self):
        from extra.view.view import View
        from extra.menu.menu_factories.concrete.menu_profile_factory import MenuProfileFactory
        view = View()
        while True:
            view.msg("Ranking")
            for option in range(len(self.options)):
                print(f"({option + 1}) - {self.options[option]}")
            view.row()
            opt = input("-> ")[0].lower()
            view.clean_prompt()
            if opt not in ["1", "2", "3"]:
                view.msg("Choose a valid option")
            elif opt == "1":
                MenuProfileFactory.create_menu().display()
            elif opt == "2":
                self._global_rank()
            else:
                return
            view.stop()
            view.clean_prompt()

    @staticmethod
    def _global_rank():
        from extra.view.view import View
        from extra.ranking.ranking import Ranking
        view = View()
        view.msg("Global Rank", 180)
        print(Ranking().get_table())
        view.row(180)
        input("Press any key to get back: ")
