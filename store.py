from base_store import BaseStore

# create a Store class
class Store(BaseStore):
    def __init__(self, items, capacity: int=100):
        super().__init__(items, capacity)
        self._capacity = 100 - sum(items.values())

    def __repr__(self):
        return 'склад'

    def add(self, name: str, amount: int):
        ...