from models import Apartment


class ApartmentCollection:
    def __init__(self, items=None):
        self._items = items or []

    def add(self, item):
        if not isinstance(item, Apartment):
            raise TypeError("Можно добавлять только Apartment")
        self._items.append(item)

    def __iter__(self):
        return iter(self._items)

    def __len__(self):
        return len(self._items)

    #  стратегия сортировки
    def sort_by(self, key_func):
        return ApartmentCollection(sorted(self._items, key=key_func))

    #  стратегия фильтрации
    def filter_by(self, predicate):
        return ApartmentCollection(list(filter(predicate, self._items)))

    #  применение функции
    def apply(self, func):
        return list(map(func, self._items))

    def __str__(self):
        return "\n".join(str(x) for x in self._items)