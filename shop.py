from base_store import BaseStore
# Create a Shop class
class Shop(BaseStore):
    def __init__(self, items, capacity: int=20):
        super().__init__(items, capacity)
        self._capacity = 20 - sum(items.values())

    def __repr__(self):
        return 'магазин'

    def add(self, name: str, amount: int):
        if self.get_unique_items_count() >= 5:
            raise TooManyDifferentProductsError
        super().add(name, amount)