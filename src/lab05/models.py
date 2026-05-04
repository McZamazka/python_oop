class Apartment:
    def __init__(self, title, area, price, address, rent_months):
        self._title = title
        self._area = area
        self._price = price
        self._address = address
        self._rent_months = rent_months

    @property
    def title(self):
        return self._title

    @property
    def area(self):
        return self._area

    @property
    def price(self):
        return self._price

    @property
    def address(self):
        return self._address

    @property
    def rent_months(self):
        return self._rent_months

    def __str__(self):
        return f"{self._title}: {self._area} м², {self._price} руб./мес."


class ResidentialApartment(Apartment):
    def __init__(self, title, area, price, address, rent_months, rooms_count, has_balcony):
        super().__init__(title, area, price, address, rent_months)
        self._rooms_count = rooms_count
        self._has_balcony = has_balcony

    def __str__(self):
        return f"Жилая квартира: {self.title}, {self.area} м², {self.price} руб./мес."


class CommercialApartment(Apartment):
    def __init__(self, title, area, price, address, rent_months, business_type, has_separate_entrance):
        super().__init__(title, area, price, address, rent_months)
        self._business_type = business_type
        self._has_separate_entrance = has_separate_entrance

    def __str__(self):
        return f"Коммерческая недвижимость: {self.title}, {self.area} м², {self.price} руб./мес."