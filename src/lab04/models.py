from interfaces import Printable, Calculable


class Apartment(Printable, Calculable):
    def __init__(self, title, area, price):
        self._title = title
        self._area = area
        self._price = price

    def calculate_income(self):
        return self._price * 12

    def display(self):
        return f"{self._title}: {self._price} руб./мес."


class ResidentialApartment(Apartment):
    def __init__(self, title, area, price, rooms):
        super().__init__(title, area, price)
        self._rooms = rooms

    def calculate_income(self):
        return super().calculate_income() * 1.05

    def display(self):
        return f"Жилая: {self._title}, {self._rooms} комнат"


class CommercialApartment(Apartment):
    def __init__(self, title, area, price, business_type):
        super().__init__(title, area, price)
        self._business_type = business_type

    def calculate_income(self):
        return super().calculate_income() * 1.2

    def display(self):
        return f"Коммерческая: {self._title}, тип: {self._business_type}"