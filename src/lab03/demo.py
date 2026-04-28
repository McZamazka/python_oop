from base import Apartment
from models import ResidentialApartment, CommercialApartment


class RealEstateCollection:
    def __init__(self):
        self._items = []

    def add(self, item):
        if not isinstance(item, Apartment):
            raise TypeError("Можно добавлять только объекты Apartment и его наследников.")
        self._items.append(item)

    def get_by_type(self, object_type):
        result = RealEstateCollection()

        for item in self._items:
            if isinstance(item, object_type):
                result.add(item)

        return result

    def __iter__(self):
        return iter(self._items)

    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __str__(self):
        if not self._items:
            return "Коллекция пуста."

        result = "Коллекция недвижимости:\n"
        for index, item in enumerate(self._items, start=1):
            result += f"{index}. {item}\n"

        return result.strip()


def main():
    print("=== Сценарий 1. Создание объектов разных типов ===")

    apartment = Apartment(
        title="Обычная квартира",
        area=35,
        price=40000,
        address="Москва, ул. Лесная, д. 7",
        rent_months=12,
    )

    residential = ResidentialApartment(
        title="Семейная квартира",
        area=60,
        price=75000,
        address="Москва, ул. Пушкина, д. 10",
        rent_months=12,
        rooms_count=3,
        has_balcony=True,
    )

    commercial = CommercialApartment(
        title="Помещение под офис",
        area=90,
        price=150000,
        address="Москва, Тверская, д. 5",
        rent_months=12,
        business_type="Офис",
        has_separate_entrance=True,
    )

    print(apartment)
    print(residential)
    print(commercial)
    print()

    print("=== Сценарий 2. Методы базового и дочерних классов ===")
    print("Общая стоимость обычной квартиры:", apartment.total_rent_cost())
    print("Подходит для семьи:", residential.is_family_friendly())
    print("Подходит для бизнеса:", commercial.is_suitable_for_business())
    print()

    print("=== Сценарий 3. Полиморфизм ===")
    objects = [apartment, residential, commercial]

    for obj in objects:
        print(obj.title, "-> доход:", obj.calculate_income())
    print()

    print("=== Сценарий 4. Единая коллекция разных типов ===")
    collection = RealEstateCollection()
    collection.add(apartment)
    collection.add(residential)
    collection.add(commercial)

    print(collection)
    print("Количество объектов:", len(collection))
    print()

    print("=== Сценарий 5. Проверка типов через isinstance() ===")
    for obj in collection:
        if isinstance(obj, ResidentialApartment):
            print(obj.title, "- жилая квартира")
        elif isinstance(obj, CommercialApartment):
            print(obj.title, "- коммерческая недвижимость")
        else:
            print(obj.title, "- базовый объект недвижимости")
    print()

    print("=== Сценарий 6. Фильтрация по типу ===")
    only_residential = collection.get_by_type(ResidentialApartment)
    print("Только жилые квартиры:")
    print(only_residential)
    print()

    only_commercial = collection.get_by_type(CommercialApartment)
    print("Только коммерческая недвижимость:")
    print(only_commercial)
    print()

    print("=== Сценарий 7. Индексация ===")
    print("Первый объект:")
    print(collection[0])
    print()

    print("=== Сценарий 8. Ошибка типа ===")
    try:
        collection.add("не недвижимость")
    except TypeError as error:
        print("Ошибка:", error)


if __name__ == "__main__":
    main()