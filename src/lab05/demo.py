
from models import ResidentialApartment, CommercialApartment
from collection import ApartmentCollection
import strategies as st


def main():
    print("=== Сценарий 1. Цепочка filter → sort → apply ===")

    collection = ApartmentCollection([
        ResidentialApartment("Квартира 1", 60, 70000, "Москва", 12, 3, True),
        ResidentialApartment("Квартира 2", 45, 50000, "Москва", 12, 2, False),
        CommercialApartment("Офис", 100, 150000, "Москва", 12, "офис", True),
        CommercialApartment("Магазин", 80, 120000, "Москва", 12, "ритейл", False),
        ResidentialApartment("Студия", 30, 40000, "Москва", 12, 1, False),
    ])

    result = (
        collection
        .filter_by(st.is_expensive)
        .sort_by(st.by_price)
    )

    print("После filter + sort:")
    print(result)
    print()

    print("Применение стратегии скидки:")
    discount = st.DiscountStrategy(0.1)
    print(result.apply(discount))
    print()

    print("=== Сценарий 2. Замена стратегии ===")

    print("Сортировка по площади:")
    print(collection.sort_by(st.by_area))
    print()

    print("Сортировка по цене за м²:")
    print(collection.sort_by(st.by_price_per_m2))
    print()

    print("=== Сценарий 3. map, filter, lambda ===")

    names = list(map(lambda x: x.title, collection))
    print("Названия:", names)

    cheap = collection.filter_by(st.make_price_filter(60000))
    print("До 60000:")
    print(cheap)


if __name__ == "__main__":
    main()