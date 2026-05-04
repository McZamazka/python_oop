
from base import Apartment


class ResidentialApartment(Apartment):
    def __init__(
        self,
        title,
        area,
        price,
        address,
        rent_months,
        rooms_count,
        has_balcony,
        status="available",
    ):
        super().__init__(title, area, price, address, rent_months, status)
        self._rooms_count = self._validate_rooms_count(rooms_count)
        self._has_balcony = self._validate_has_balcony(has_balcony)

    @staticmethod
    def _validate_rooms_count(value):
        if not isinstance(value, int):
            raise TypeError("Количество комнат должно быть целым числом.")
        if value <= 0:
            raise ValueError("Количество комнат должно быть больше 0.")
        return value

    @staticmethod
    def _validate_has_balcony(value):
        if not isinstance(value, bool):
            raise TypeError("Наличие балкона должно быть True или False.")
        return value

    @property
    def rooms_count(self):
        return self._rooms_count

    @property
    def has_balcony(self):
        return self._has_balcony

    def is_family_friendly(self):
        return self._rooms_count >= 2

    def calculate_income(self):
        bonus = 1.05 if self._has_balcony else 1
        return self.total_rent_cost() * bonus

    def __str__(self):
        balcony = "есть балкон" if self._has_balcony else "без балкона"
        return (
            f"Жилая квартира: {self._title}, {self._area:.1f} м², "
            f"{self._price:.2f} руб./мес., комнат: {self._rooms_count}, "
            f"{balcony}, статус: {self._status}"
        )


class CommercialApartment(Apartment):
    def __init__(
        self,
        title,
        area,
        price,
        address,
        rent_months,
        business_type,
        has_separate_entrance,
        status="available",
    ):
        super().__init__(title, area, price, address, rent_months, status)
        self._business_type = self._validate_business_type(business_type)
        self._has_separate_entrance = self._validate_has_separate_entrance(
            has_separate_entrance
        )

    @staticmethod
    def _validate_business_type(value):
        if not isinstance(value, str):
            raise TypeError("Тип бизнеса должен быть строкой.")
        if not value.strip():
            raise ValueError("Тип бизнеса не может быть пустым.")
        return value.strip()

    @staticmethod
    def _validate_has_separate_entrance(value):
        if not isinstance(value, bool):
            raise TypeError("Наличие отдельного входа должно быть True или False.")
        return value

    @property
    def business_type(self):
        return self._business_type

    @property
    def has_separate_entrance(self):
        return self._has_separate_entrance

    def is_suitable_for_business(self):
        return self._has_separate_entrance

    def calculate_income(self):
        bonus = 1.15 if self._has_separate_entrance else 1
        return self.total_rent_cost() * bonus

    def __str__(self):
        entrance = "отдельный вход" if self._has_separate_entrance else "общий вход"
        return (
            f"Коммерческая недвижимость: {self._title}, {self._area:.1f} м², "
            f"{self._price:.2f} руб./мес., бизнес: {self._business_type}, "
            f"{entrance}, статус: {self._status}"
        )