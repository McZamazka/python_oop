class Apartment:
    property_type = "Жилая недвижимость"

    AVAILABLE_STATUS = "available"
    RENTED_STATUS = "rented"
    ARCHIVED_STATUS = "archived"

    def __init__(self, title, area, price, address, rent_months, status="available"):
        self._title = self._validate_title(title)
        self._area = self._validate_area(area)
        self._price = self._validate_price(price)
        self._address = self._validate_address(address)
        self._rent_months = self._validate_rent_months(rent_months)
        self._status = self._validate_status(status)

    @staticmethod
    def _validate_title(value):
        if not isinstance(value, str):
            raise TypeError("Название должно быть строкой.")
        if not value.strip():
            raise ValueError("Название не может быть пустым.")
        return value.strip()

    @staticmethod
    def _validate_area(value):
        if not isinstance(value, (int, float)):
            raise TypeError("Площадь должна быть числом.")
        if value <= 0:
            raise ValueError("Площадь должна быть больше 0.")
        return float(value)

    @staticmethod
    def _validate_price(value):
        if not isinstance(value, (int, float)):
            raise TypeError("Цена должна быть числом.")
        if value <= 0:
            raise ValueError("Цена должна быть больше 0.")
        return float(value)

    @staticmethod
    def _validate_address(value):
        if not isinstance(value, str):
            raise TypeError("Адрес должен быть строкой.")
        if not value.strip():
            raise ValueError("Адрес не может быть пустым.")
        return value.strip()

    @staticmethod
    def _validate_rent_months(value):
        if not isinstance(value, int):
            raise TypeError("Срок аренды должен быть целым числом.")
        if value <= 0:
            raise ValueError("Срок аренды должен быть больше 0.")
        return value

    @classmethod
    def _validate_status(cls, value):
        if not isinstance(value, str):
            raise TypeError("Статус должен быть строкой.")

        allowed_statuses = {
            cls.AVAILABLE_STATUS,
            cls.RENTED_STATUS,
            cls.ARCHIVED_STATUS,
        }

        if value not in allowed_statuses:
            raise ValueError("Недопустимый статус квартиры.")

        return value

    @property
    def title(self):
        return self._title

    @property
    def area(self):
        return self._area

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        self._price = self._validate_price(new_price)

    @property
    def address(self):
        return self._address

    @property
    def rent_months(self):
        return self._rent_months

    @rent_months.setter
    def rent_months(self, new_rent_months):
        self._rent_months = self._validate_rent_months(new_rent_months)

    @property
    def status(self):
        return self._status

    def monthly_price_per_m2(self):
        return self._price / self._area

    def total_rent_cost(self):
        return self._price * self._rent_months

    def rent(self):
        if self._status == self.RENTED_STATUS:
            raise ValueError("Квартира уже сдана.")
        if self._status == self.ARCHIVED_STATUS:
            raise ValueError("Архивную квартиру нельзя сдать.")
        self._status = self.RENTED_STATUS

    def archive(self):
        if self._status == self.RENTED_STATUS:
            raise ValueError("Нельзя архивировать сданную квартиру.")
        self._status = self.ARCHIVED_STATUS

    def reopen(self):
        if self._status != self.ARCHIVED_STATUS:
            raise ValueError("Открыть заново можно только архивную квартиру.")
        self._status = self.AVAILABLE_STATUS

    def __str__(self):
        return (
            f"{self._title}: {self._area:.1f} м², "
            f"{self._price:.2f} руб./мес., "
            f"{self._address}, срок: {self._rent_months} мес., "
            f"статус: {self._status}"
        )

    def __repr__(self):
        return (
            f"Apartment(title={self._title!r}, area={self._area!r}, "
            f"price={self._price!r}, address={self._address!r}, "
            f"rent_months={self._rent_months!r}, status={self._status!r})"
        )

    def __eq__(self, other):
        if not isinstance(other, Apartment):
            return False

        return (
            self._title == other._title
            and self._area == other._area
            and self._price == other._price
            and self._address == other._address
            and self._rent_months == other._rent_months
            and self._status == other._status
        )