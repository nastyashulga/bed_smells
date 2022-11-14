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


# create a Store class
class Store(Storage):
    def __init__(self, items):
        super().__init__(items)
        self._capacity = 100 - sum(items.values())

    def __repr__(self):
        return 'склад'

    def add(self, name, amount):
        if amount <= self._capacity:
            self._items[name] = self._items.get(name, 0) + amount
            self._capacity -= amount

    def remove(self, name, amount, storage):
        if amount > storage.get_free_space():
            raise NotEnoughSpaceError

        if storage == 'магазин' and storage.get_unique_items_count() >= 5:
            raise MoreThanFiveUniquesError

        if name not in self._items:
            raise UnknownItemError

        elif amount <= self._items.get(name):
            self._items[name] = self._items.get(name) - amount
            self._capacity += amount
            if self._items[name] == 0:
                del self._items[name]

        else:
            raise NotEnoughItemError

    def get_free_space(self):
        return self._capacity

    def get_items(self):
        return self._items

    def get_unique_items_count(self):
        return len(self.get_items())


# Create a Shop class
class Shop(Storage):
    def __init__(self, items):
        super().__init__(items)
        self._capacity = 20 - sum(items.values())

    def __repr__(self):
        return 'магазин'

    def add(self, name, amount):

        self._items[name] = self._items.get(name, 0) + amount
        self._capacity -= amount


    def remove(self, name, amount, storage):
        if amount > storage.get_free_space():
            raise NotEnoughSpaceError

        if storage == 'магазин' and storage.get_unique_items_count() >= 5:
            raise MoreThanFiveUniquesError

        if name not in self._items:
            raise UnknownItemError

        elif amount <= self._items.get(name):
            self._items[name] = self._items.get(name) - amount
            self._capacity += amount
            if self._items[name] == 0:
                del self._items[name]

        else:
            raise NotEnoughItemError

    def get_free_space(self):
        return self._capacity

    def get_items(self):
        return self._items

    def get_unique_items_count(self):
        return len(self._items)


# create a Request class
class Request:
    def __init__(self, user_string, list_of_shops):
        request_split = user_string.split(' ')

        self.amount = int(request_split[1])
        self.product = request_split[2]
        self.departure = request_split[4]
        self.destination = request_split[6]

        if self.destination not in list_of_shops or self.departure not in list_of_shops:
            raise UnknownStorageError
