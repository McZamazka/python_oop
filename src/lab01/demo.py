from model import Apartment


def main():
    print("=== Сценарий 1. Создание объекта и вывод ===")
    apartment1 = Apartment(
        title="Студия у метро",
        area=28.5,
        price=45000,
        address="Москва, ул. Пушкина, д. 10",
        rent_months=12
    )
    print(apartment1)
    print("Цена за 1 м² в месяц:", f"{apartment1.monthly_price_per_m2():.2f} руб.")
    print("Полная стоимость аренды:", f"{apartment1.total_rent_cost():.2f} руб.")
    print()

    print("=== Сценарий 2. Сравнение объектов ===")
    apartment2 = Apartment(
        title="Студия у метро",
        area=28.5,
        price=45000,
        address="Москва, ул. Пушкина, д. 10",
        rent_months=12
    )
    apartment3 = Apartment(
        title="Двушка в центре",
        area=54.0,
        price=80000,
        address="Москва, Тверская, д. 5",
        rent_months=6
    )

    print("apartment1 == apartment2 ->", apartment1 == apartment2)
    print("apartment1 == apartment3 ->", apartment1 == apartment3)
    print()

    print("=== Сценарий 3. Setter и валидация ===")
    print("Старая цена:", apartment1.price)
    apartment1.price = 50000
    print("Новая цена:", apartment1.price)

    try:
        apartment1.price = -1000
    except (TypeError, ValueError) as error:
        print("Ошибка при изменении цены:", error)
    print()

    print("=== Сценарий 4. Атрибут класса ===")
    print("Через класс:", Apartment.property_type)
    print("Через экземпляр:", apartment1.property_type)
    print()

    print("=== Сценарий 5. Изменение состояния объекта ===")
    print("Начальный статус:", apartment1.status)
    apartment1.rent()
    print("После rent():", apartment1.status)

    try:
        apartment1.archive()
    except ValueError as error:
        print("Ошибка при archive():", error)

    try:
        apartment1.rent()
    except ValueError as error:
        print("Ошибка при повторной сдаче:", error)
    print()

    print("=== Сценарий 6. Работа с архивом ===")
    apartment4 = Apartment(
        title="Однушка на окраине",
        area=35,
        price=30000,
        address="Москва, ул. Лесная, д. 7",
        rent_months=10
    )
    print("Статус apartment4:", apartment4.status)
    apartment4.archive()
    print("После archive():", apartment4.status)

    try:
        apartment4.rent()
    except ValueError as error:
        print("Ошибка при rent() для архивной квартиры:", error)

    apartment4.reopen()
    print("После reopen():", apartment4.status)
    print()

    print("=== Сценарий 7. Некорректное создание объекта ===")
    try:
        bad_apartment = Apartment(
            title="",
            area=-20,
            price="дёшево",
            address="",
            rent_months=0
        )
        print(bad_apartment)
    except (TypeError, ValueError) as error:
        print("Ошибка при создании объекта:", error)


if __name__ == "__main__":
    main()