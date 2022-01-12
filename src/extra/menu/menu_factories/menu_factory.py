from abc import ABC, abstractmethod


class MenuFactory(ABC):
    __slots__ = ["_menu_obj"]

    def __init__(self):
        self._menu_obj = None

    @abstractmethod
    def create_menu(self):
        """
        Creates a menu specified by the class implementing
        this interface
        :return:  the created menu
        """
