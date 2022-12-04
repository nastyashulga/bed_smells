from abstract_store import Storage

class BaseStore(Storage):
    def __init__(self, items, capacity):
        self._items = items
        self._capacity = capacity

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