from abc import ABC, abstractmethod
from extra.menu.menus.menu import Menu


class MenuFactory(ABC):
    _menu_obj = None

    @classmethod
    @abstractmethod
    def create_menu(cls):
        """
        Creates a menu specified by the class implementing
        this interface and records it in variable _menu_obj,
        so that it can be retrieved more than once
        :return:  the created menu
        """

    @classmethod
    def set_menu_obj(cls, menu_obj: Menu):
        cls._menu_obj = menu_obj

    @classmethod
    def get_menu_obj(cls):
        return cls._menu_obj
