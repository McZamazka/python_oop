# сортировки

def by_price(apartment):
    return apartment.price


def by_area(apartment):
    return apartment.area


def by_price_per_m2(apartment):
    return apartment.price / apartment.area


#  фильтры

def is_expensive(apartment):
    return apartment.price > 70000


def is_large(apartment):
    return apartment.area > 50


def is_residential(apartment):
    from models import ResidentialApartment
    return isinstance(apartment, ResidentialApartment)


#  фабрика функций

def make_price_filter(max_price):
    def filter_fn(apartment):
        return apartment.price <= max_price
    return filter_fn


#  стратегия (callable объект)

class DiscountStrategy:
    def __init__(self, percent):
        self._percent = percent

    def __call__(self, apartment):
        return apartment.price * (1 - self._percent)