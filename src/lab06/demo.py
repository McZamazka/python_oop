from container import Displayable, Scorable, TypedCollection


class Apartment:
    def __init__(
        self,
        title: str,
        area: float,
        price: float,
        address: str,
        rent_months: int,
    ) -> None:
        self._title: str = title
        self._area: float = area
        self._price: float = price
        self._address: str = address
        self._rent_months: int = rent_months

    @property
    def title(self) -> str:
        return self._title

    @property
    def area(self) -> float:
        return self._area

    @property
    def price(self) -> float:
        return self._price

    @property
    def address(self) -> str:
        return self._address

    @property
    def rent_months(self) -> int:
        return self._rent_months

    def total_rent_cost(self) -> float:
        return self._price * self._rent_months

    def display(self) -> str:
        return f"{self._title}: {self._area} м², {self._price} руб./мес."

    def score(self) -> float:
        return self.total_rent_cost()

    def __str__(self) -> str:
        return self.display()


class ResidentialApartment(Apartment):
    def __init__(
        self,
        title: str,
        area: float,
        price: float,
        address: str,
        rent_months: int,
        rooms_count: int,
    ) -> None:
        super().__init__(title, area, price, address, rent_months)
        self._rooms_count: int = rooms_count

    def display(self) -> str:
        return f"Жилая квартира: {self.title}, комнат: {self._rooms_count}, цена: {self.price}"

    def score(self) -> float:
        return self.total_rent_cost() * 1.05


class CommercialApartment(Apartment):
    def __init__(
        self,
        title: str,
        area: float,
        price: float,
        address: str,
        rent_months: int,
        business_type: str,
    ) -> None:
        super().__init__(title, area, price, address, rent_months)
        self._business_type: str = business_type

    def display(self) -> str:
        return f"Коммерческая недвижимость: {self.title}, тип: {self._business_type}, цена: {self.price}"

    def score(self) -> float:
        return self.total_rent_cost() * 1.2


def print_collection(collection: TypedCollection[Apartment]) -> None:
    for item in collection:
        print(item.display())


def main() -> None:
    print("=== Сценарий 1. TypedCollection[Apartment] ===")

    apartments: TypedCollection[Apartment] = TypedCollection(Apartment)

    apartment1 = ResidentialApartment("Семейная квартира", 60, 75000, "Москва", 12, 3)
    apartment2 = ResidentialApartment("Студия", 30, 45000, "Москва", 12, 1)
    apartment3 = CommercialApartment("Офис", 90, 150000, "Москва", 12, "офис")

    apartments.add(apartment1)
    apartments.add(apartment2)
    apartments.add(apartment3)

    print("Все объекты:")
    print_collection(apartments)
    print()

    print("Проверка типа при добавлении:")
    try:
        apartments.add("не квартира")
    except TypeError as error:
        print("Ошибка:", error)
    print()

    print("=== Сценарий 2. find(), filter(), map() ===")

    found = apartments.find(lambda item: item.price > 100000)
    print("Найден объект дороже 100000:")
    print(found.display() if found else None)

    not_found = apartments.find(lambda item: item.price > 300000)
    print("Поиск объекта дороже 300000:")
    print(not_found)
    print()

    expensive = apartments.filter(lambda item: item.price >= 70000)
    print("Фильтр: объекты от 70000:")
    print_collection(expensive)
    print()

    titles: list[str] = apartments.map(lambda item: item.title)
    prices: list[float] = apartments.map(lambda item: item.price)

    print("map() -> list[str]:", titles)
    print("map() -> list[float]:", prices)
    print()

    print("=== Сценарий 3. Protocol Displayable ===")

    displayable_items: TypedCollection[Displayable] = TypedCollection(Displayable)

    displayable_items.add(apartment1)
    displayable_items.add(apartment3)

    for item in displayable_items:
        print(item.display())
    print()

    print("=== Сценарий 4. Protocol Scorable ===")

    scorable_items: TypedCollection[Scorable] = TypedCollection(Scorable)

    scorable_items.add(apartment1)
    scorable_items.add(apartment2)
    scorable_items.add(apartment3)

    for item in scorable_items:
        print(item.score())


if __name__ == "__main__":
    main()