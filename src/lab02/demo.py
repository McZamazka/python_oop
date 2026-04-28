from model import Apartment
from collection import ApartmentCollection


def print_collection(title, collection):
    print(title)
    print(collection)
    print()


def main():
    print("=== Сценарий 1. Создание коллекции и добавление объектов ===")

    apartment1 = Apartment(
        title="Студия у метро",
        area=28.5,
        price=45000,
        address="Москва, ул. Пушкина, д. 10",
        rent_months=12,
    )

    apartment2 = Apartment(
        title="Двушка в центре",
        area=54.0,
        price=80000,
        address="Москва, Тверская, д. 5",
        rent_months=6,
    )

    apartment3 = Apartment(
        title="Однушка на окраине",
        area=35.0,
        price=30000,
        address="Москва, ул. Лесная, д. 7",
        rent_months=10,
    )

    apartment4 = Apartment(
        title="Апартаменты бизнес-класса",
        area=72.0,
        price=120000,
        address="Москва, Пресненская наб., д. 12",
        rent_months=12,
    )

    collection = ApartmentCollection()

    collection.add(apartment1)
    collection.add(apartment2)
    collection.add(apartment3)
    collection.add(apartment4)

    print_collection("Все квартиры:", collection)

    print("=== Сценарий 2. len() и итерация через for ===")
    print("Количество квартир:", len(collection))

    for apartment in collection:
        print(apartment.title, "-", apartment.price, "руб./мес.")
    print()

    print("=== Сценарий 3. Поиск объектов ===")
    found_by_title = collection.find_by_title("Студия у метро")
    print_collection("Результат поиска по названию:", found_by_title)

    found_by_address = collection.find_by_address("Москва")
    print_collection("Результат поиска по адресу:", found_by_address)

    print("=== Сценарий 4. Проверка ограничения на дубликаты ===")
    try:
        collection.add(apartment1)
    except ValueError as error:
        print("Ошибка при добавлении дубликата:", error)
    print()

    print("=== Сценарий 5. Проверка типа добавляемого объекта ===")
    try:
        collection.add("Это не квартира")
    except TypeError as error:
        print("Ошибка при добавлении объекта неправильного типа:", error)
    print()

    print("=== Сценарий 6. Индексация коллекции ===")
    print("Первый элемент collection[0]:")
    print(collection[0])
    print()

    print("=== Сценарий 7. Сортировка по цене ===")
    collection.sort_by_price()
    print_collection("После сортировки по цене:", collection)

    print("=== Сценарий 8. Фильтрация дорогих квартир ===")
    expensive = collection.get_expensive(70000)
    print_collection("Квартиры дороже 70000 руб./мес.:", expensive)

    print("=== Сценарий 9. Фильтрация доступных квартир ===")
    apartment2.rent()
    available = collection.get_available()
    print_collection("Доступные квартиры:", available)

    print("=== Сценарий 10. Удаление объекта ===")
    collection.remove(apartment3)
    print_collection("После удаления apartment3:", collection)

    print("=== Сценарий 11. Удаление по индексу ===")
    removed = collection.remove_at(0)
    print("Удалённый объект:", removed)
    print_collection("После удаления по индексу:", collection)


if __name__ == "__main__":
    main()