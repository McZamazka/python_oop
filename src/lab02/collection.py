from model import Apartment


class ApartmentCollection:
    def __init__(self):
        self._items = []

    def add(self, item):
        if not isinstance(item, Apartment):
            raise TypeError("В коллекцию можно добавлять только объекты Apartment.")

        if item in self._items:
            raise ValueError("Такая квартира уже есть в коллекции.")

        self._items.append(item)

    def remove(self, item):
        if item not in self._items:
            raise ValueError("Такой квартиры нет в коллекции.")

        self._items.remove(item)

    def remove_at(self, index):
        if not isinstance(index, int):
            raise TypeError("Индекс должен быть целым числом.")

        if index < 0 or index >= len(self._items):
            raise IndexError("Индекс выходит за границы коллекции.")

        return self._items.pop(index)

    def get_all(self):
        return self._items.copy()

    def find_by_title(self, title):
        if not isinstance(title, str):
            raise TypeError("Название должно быть строкой.")

        result = ApartmentCollection()

        for apartment in self._items:
            if apartment.title.lower() == title.lower():
                result.add(apartment)

        return result

    def find_by_address(self, address):
        if not isinstance(address, str):
            raise TypeError("Адрес должен быть строкой.")

        result = ApartmentCollection()

        for apartment in self._items:
            if address.lower() in apartment.address.lower():
                result.add(apartment)

        return result

    def sort_by_price(self):
        self._items.sort(key=lambda apartment: apartment.price)

    def sort_by_area(self):
        self._items.sort(key=lambda apartment: apartment.area)

    def sort(self, key):
        self._items.sort(key=key)

    def get_available(self):
        result = ApartmentCollection()

        for apartment in self._items:
            if apartment.status == Apartment.AVAILABLE_STATUS:
                result.add(apartment)

        return result

    def get_expensive(self, min_price):
        if not isinstance(min_price, (int, float)):
            raise TypeError("Минимальная цена должна быть числом.")

        result = ApartmentCollection()

        for apartment in self._items:
            if apartment.price >= min_price:
                result.add(apartment)

        return result

    def get_large(self, min_area):
        if not isinstance(min_area, (int, float)):
            raise TypeError("Минимальная площадь должна быть числом.")

        result = ApartmentCollection()

        for apartment in self._items:
            if apartment.area >= min_area:
                result.add(apartment)

        return result

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __str__(self):
        if not self._items:
            return "Коллекция квартир пуста."

        result = "Коллекция квартир:\n"

        for index, apartment in enumerate(self._items, start=1):
            result += f"{index}. {apartment}\n"

        return result.strip()