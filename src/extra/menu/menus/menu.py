# Menus: player logged in, player logged out, account creation
# Use Abstract Factory pattern.
from abc import ABC, abstractmethod
from extra.view.view import View


class Menu(ABC):

    def __init__(self, *options):
        assert len(options) > 0, f"Options cannot be empty"
        self._options = options

    @abstractmethod
    def display(self):
        """
        This method handles each option defined for
        this menu by its index starting from 1 towards
        len(self._options) which is the quantity of
        options for this menu.
        :return: nothing
        """

    @staticmethod
    def get_out():
        from sys import exit
        view = View()
        view.msg("Are you sure? [y/n]", 150)
        if input("-> ")[0].lower() == "y":
            view.clean_prompt()
            view.msg("Good bye!", 150)
            view.stop(2)
            view.clean_prompt()
            exit()  # Shuts PVM down.
        view.clean_prompt()

    @property
    def options(self):
        return self._options
