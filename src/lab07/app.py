from models import Apartment
from exceptions import DuplicateApartmentError, ApartmentNotFoundError


class ApartmentApp:
    def __init__(self, apartments: list[Apartment] | None = None) -> None:
        self._apartments: list[Apartment] = apartments or []

    def add_apartment(
        self,
        title: str,
        area: float,
        price: float,
        address: str,
        rent_months: int,
    ) -> None:
        """Создаёт и добавляет квартиру в коллекцию."""
        apartment = Apartment(
            title=title,
            area=area,
            price=price,
            address=address,
            rent_months=rent_months,
        )

        if apartment in self._apartments:
            raise DuplicateApartmentError("Такая квартира уже есть.")

        self._apartments.append(apartment)

    def get_all(self) -> list[Apartment]:
        """Возвращает все квартиры."""
        return list(self._apartments)

    def find_by_title(self, title: str) -> list[Apartment]:
        """Ищет квартиры по названию."""
        return [
            apartment
            for apartment in self._apartments
            if title.lower() in apartment.title.lower()
        ]

    def find_by_address(self, address: str) -> list[Apartment]:
        """Ищет квартиры по адресу."""
        return [
            apartment
            for apartment in self._apartments
            if address.lower() in apartment.address.lower()
        ]

    def filter_by_status(self, status: str) -> list[Apartment]:
        """Фильтрует квартиры по статусу."""
        return [
            apartment
            for apartment in self._apartments
            if apartment.status == status
        ]

    def filter_by_price_range(
        self,
        min_price: float,
        max_price: float,
    ) -> list[Apartment]:
        """Фильтрует квартиры по диапазону цены."""
        return [
            apartment
            for apartment in self._apartments
            if min_price <= apartment.price <= max_price
        ]

    def sort_by_title(self) -> list[Apartment]:
        """Сортирует квартиры по названию."""
        return sorted(
            self._apartments,
            key=lambda apartment: apartment.title,
        )

    def sort_by_price(self) -> list[Apartment]:
        """Сортирует квартиры по цене."""
        return sorted(
            self._apartments,
            key=lambda apartment: apartment.price,
        )

    def sort_by_area(self) -> list[Apartment]:
        """Сортирует квартиры по площади."""
        return sorted(
            self._apartments,
            key=lambda apartment: apartment.area,
        )

    def rent_apartment(self, index: int) -> None:
        """Сдаёт квартиру по индексу."""
        apartment = self._get_by_index(index)
        apartment.rent()

    def archive_apartment(self, index: int) -> None:
        """Архивирует квартиру по индексу."""
        apartment = self._get_by_index(index)
        apartment.archive()

    def delete_apartment(self, index: int) -> Apartment:
        """Удаляет квартиру по индексу."""
        if index < 0 or index >= len(self._apartments):
            raise ApartmentNotFoundError("Квартира не найдена.")

        return self._apartments.pop(index)

    def _get_by_index(self, index: int) -> Apartment:
        if index < 0 or index >= len(self._apartments):
            raise ApartmentNotFoundError("Квартира не найдена.")

        return self._apartments[index]