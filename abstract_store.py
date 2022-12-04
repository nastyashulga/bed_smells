from abc import ABC, abstractmethod

from storages_exceptions import NotEnoughSpaceError, UnknownItemError, NotEnoughItemError, MoreThanFiveUniquesError, \
    UnknownStorageError


# create an abstract Class
class Storage(ABC):
    def __init__(self, items):
        self._items = items

    def __repr__(self):
        return 'Некий магазин'

    @abstractmethod
    def add(self, name, amount):
        pass

    @abstractmethod
    def remove(self, name, amount, storage):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass









