from abc import ABC, abstractmethod


class Storage(ABC):
    def __init__(self):
        self._items = {}
        self._capacity = 0

    @abstractmethod
    def add(self, name, amount):
        pass

    @abstractmethod
    def remove(self, name, amount):
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





class Store(Storage):
    def __init__(self):
        super().__init__()
        self._capacity = 100

    def add(self, name, amount):
        if amount < self._capacity:
            self._items[name] = self._items.get(name, 0) + amount
            self._capacity -= amount

        elif amount >= self._capacity:
            difference = amount - self._capacity
            self._items[name] = self._items.get(name, 0) + self._capacity
            self._capacity = 0

    def remove(self, name, amount):
        if name not in self._items:
            return 'Такого товара нет в магазине'

        elif amount < self._items.get(name):
            self._items[name] = self._items.get(name) - amount
            self._capacity += amount

        else:
            difference = amount - self._items.get(name)
            self._capacity += self._items.get(name)
            del self._items[name]

    def get_free_space(self):
        return self._capacity

    def get_items(self):
        return self._items

    def get_unique_items_count(self):
        return len(self.get_items())


class Shop(Storage):
    def __init__(self):
        super().__init__()
        self._capacity = 20

    def add(self, name, amount):
        if self.get_unique_items_count() >= 5:
            return 'В магазине уже 5 уникальных товаров'
        else:
            if amount < self._capacity:
                self._items[name] = self._items.get(name, 0) + amount
                self._capacity -= amount

            elif amount >= self._capacity:
                difference = amount - self._capacity
                self._items[name] = self._items.get(name, 0) + self._capacity
                self._capacity = 0

    def remove(self, name, amount):
        if name not in self._items:
            return 'Такого товара нет в магазине'

        elif amount < self._items.get(name):
            self._items[name] = self._items.get(name) - amount
            self._capacity += amount

        else:
            difference = amount - self._items.get(name)
            self._capacity += self._items.get(name)
            del self._items[name]

    def get_free_space(self):
        return self._capacity

    def get_items(self):
        return self._items

    def get_unique_items_count(self):
        return len(self._items)


class Request:
    pass


store_1 = Shop()

store_1.add(name="картошка", amount=1)
print(store_1.get_items())
print(store_1.get_free_space())
print(store_1.get_unique_items_count())
store_1.add(name="морковка", amount=1)
print(store_1.get_items())
print(store_1.get_free_space())
print(store_1.get_unique_items_count())
store_1.add(name="свекла", amount=1)
print(store_1.get_items())
print(store_1.get_free_space())
print(store_1.get_unique_items_count())
store_1.add(name="редька", amount=1)
print(store_1.get_items())
print(store_1.get_free_space())
print(store_1.get_unique_items_count())
store_1.add(name="лук", amount=1)
print(store_1.get_items())
print(store_1.get_free_space())
print(store_1.get_unique_items_count())
store_1.add(name="сельдерей", amount=1)
print(store_1.get_items())
print(store_1.get_free_space())
print(store_1.get_unique_items_count())
store_1.add(name="помидоры", amount=1)
print(store_1.get_items())
print(store_1.get_free_space())
print(store_1.get_unique_items_count())
store_1.add(name="огурцы", amount=1)
print(store_1.get_items())
print(store_1.get_free_space())

print(store_1.get_unique_items_count())



