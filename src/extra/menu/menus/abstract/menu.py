# Menus: player logged in, player logged out, account creation
# Use Abstract Factory pattern.
from abc import ABC, abstractmethod


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

    @property
    def options(self):
        return self._options
