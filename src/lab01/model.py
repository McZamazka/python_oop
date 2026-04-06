from validate import (
    validate_title,
    validate_area,
    validate_price,
    validate_address,
    validate_rent_months,
    validate_status,
)


class Apartment:
    """
    Класс Apartment описывает квартиру для аренды.
    """

    property_type = "Жилая недвижимость"

    def __init__(self, title, area, price, address, rent_months, status="available"):
        self._title = validate_title(title)
        self._area = validate_area(area)
        self._price = validate_price(price)
        self._address = validate_address(address)
        self._rent_months = validate_rent_months(rent_months)
        self._status = validate_status(status)

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
        self._price = validate_price(new_price)

    @property
    def address(self):
        return self._address

    @property
    def rent_months(self):
        return self._rent_months

    @rent_months.setter
    def rent_months(self, new_rent_months):
        self._rent_months = validate_rent_months(new_rent_months)

    @property
    def status(self):
        return self._status

    def monthly_price_per_m2(self):
        return self._price / self._area

    def total_rent_cost(self):
        return self._price * self._rent_months

    def rent(self):
        if self._status == "rented":
            raise ValueError("Квартира уже сдана в аренду.")
        if self._status == "archived":
            raise ValueError("Архивную квартиру нельзя сдать в аренду.")
        self._status = "rented"

    def archive(self):
        if self._status == "rented":
            raise ValueError("Нельзя архивировать квартиру, пока она сдана в аренду.")
        self._status = "archived"

    def reopen(self):
        if self._status != "archived":
            raise ValueError("Открыть заново можно только архивную квартиру.")
        self._status = "available"

    def __str__(self):
        status_names = {
            "available": "доступна",
            "rented": "сдана",
            "archived": "в архиве",
        }
        return (
            f"Квартира '{self._title}': {self._area:.1f} м², "
            f"{self._price:,.2f} руб./мес., адрес: {self._address}, "
            f"срок аренды: {self._rent_months} мес., статус: {status_names[self._status]}"
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