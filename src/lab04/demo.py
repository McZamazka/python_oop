from models import Apartment, ResidentialApartment, CommercialApartment
from interfaces import Printable, Calculable


class RealEstateCollection:
    def __init__(self):
        self._items = []

    def add(self, item):
        self._items.append(item)

    def get_printable(self):
        return [item for item in self._items if isinstance(item, Printable)]

    def get_calculable(self):
        return [item for item in self._items if isinstance(item, Calculable)]

    def __iter__(self):
        return iter(self._items)


# универсальная функция через интерфейс
def print_all(items: list[Printable]):
    for item in items:
        print(item.display())


def main():
    print("=== Сценарий 1. Разные объекты ===")

    a = Apartment("Квартира", 30, 40000)
    r = ResidentialApartment("Семейная", 60, 70000, 3)
    c = CommercialApartment("Офис", 100, 150000, "офис")

    items = [a, r, c]

    print_all(items)
    print()

    print("=== Сценарий 2. Полиморфизм ===")
    for obj in items:
        print(obj.calculate_income())
    print()

    print("=== Сценарий 3. Коллекция и фильтрация ===")
    collection = RealEstateCollection()

    collection.add(a)
    collection.add(r)
    collection.add(c)

    print("Только Printable:")
    for obj in collection.get_printable():
        print(obj.display())

    print()

    print("Проверка isinstance:")
    for obj in collection:
        print(obj, "-> Printable:", isinstance(obj, Printable))


if __name__ == "__main__":
    main()