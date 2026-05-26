class Apartment:
    AVAILABLE_STATUS = "available"
    RENTED_STATUS = "rented"
    ARCHIVED_STATUS = "archived"

    def __init__(
        self,
        title: str,
        area: float,
        price: float,
        address: str,
        rent_months: int,
        status: str = AVAILABLE_STATUS,
    ) -> None:
        self._title = self._validate_text(title, "Название")
        self._area = self._validate_positive_number(area, "Площадь")
        self._price = self._validate_positive_number(price, "Цена")
        self._address = self._validate_text(address, "Адрес")
        self._rent_months = self._validate_positive_int(rent_months, "Срок аренды")
        self._status = self._validate_status(status)

    @staticmethod
    def _validate_text(value: str, field_name: str) -> str:
        if not isinstance(value, str):
            raise ValueError(f"{field_name} должно быть строкой.")
        value = value.strip()
        if not value:
            raise ValueError(f"{field_name} не может быть пустым.")
        return value

    @staticmethod
    def _validate_positive_number(value: float, field_name: str) -> float:
        if not isinstance(value, (int, float)):
            raise ValueError(f"{field_name} должно быть числом.")
        if value <= 0:
            raise ValueError(f"{field_name} должно быть больше 0.")
        return float(value)

    @staticmethod
    def _validate_positive_int(value: int, field_name: str) -> int:
        if not isinstance(value, int):
            raise ValueError(f"{field_name} должен быть целым числом.")
        if value <= 0:
            raise ValueError(f"{field_name} должен быть больше 0.")
        return value

    @classmethod
    def _validate_status(cls, value: str) -> str:
        allowed = {
            cls.AVAILABLE_STATUS,
            cls.RENTED_STATUS,
            cls.ARCHIVED_STATUS,
        }

        if value not in allowed:
            raise ValueError("Недопустимый статус квартиры.")

        return value

    @property
    def title(self) -> str:
        return self._title

    @property
    def area(self) -> float:
        return self._area

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        self._price = self._validate_positive_number(value, "Цена")

    @property
    def address(self) -> str:
        return self._address

    @property
    def rent_months(self) -> int:
        return self._rent_months

    @property
    def status(self) -> str:
        return self._status

    def total_rent_cost(self) -> float:
        """Возвращает полную стоимость аренды за весь срок."""
        return self._price * self._rent_months

    def price_per_meter(self) -> float:
        """Возвращает цену аренды за 1 м²."""
        return self._price / self._area

    def rent(self) -> None:
        """Переводит квартиру в состояние сданной."""
        if self._status == self.RENTED_STATUS:
            raise ValueError("Квартира уже сдана.")
        if self._status == self.ARCHIVED_STATUS:
            raise ValueError("Архивную квартиру нельзя сдать.")
        self._status = self.RENTED_STATUS

    def archive(self) -> None:
        """Переводит квартиру в архив."""
        if self._status == self.RENTED_STATUS:
            raise ValueError("Нельзя архивировать сданную квартиру.")
        self._status = self.ARCHIVED_STATUS

    def to_dict(self) -> dict:
        """Преобразует объект в словарь для сохранения."""
        return {
            "title": self._title,
            "area": self._area,
            "price": self._price,
            "address": self._address,
            "rent_months": self._rent_months,
            "status": self._status,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Apartment":
        """Создаёт объект Apartment из словаря."""
        return cls(
            title=data["title"],
            area=data["area"],
            price=data["price"],
            address=data["address"],
            rent_months=data["rent_months"],
            status=data["status"],
        )

    def __str__(self) -> str:
        return (
            f"{self._title} | {self._area:.1f} м² | "
            f"{self._price:.0f} руб./мес. | {self._address} | "
            f"{self._rent_months} мес. | {self._status}"
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Apartment):
            return False
        return self._title == other.title and self._address == other.address