from app import ApartmentApp
from exceptions import ApartmentAppError
from models import Apartment
from storage import save_apartments


class ApartmentCLI:
    def __init__(self, app: ApartmentApp, storage_path: str) -> None:
        self._app = app
        self._storage_path = storage_path

    def run(self) -> None:
        """Запускает главное меню приложения."""
        while True:
            self._print_menu()

            try:
                choice = int(input("Выберите пункт: "))
            except ValueError:
                print("Ошибка: введите число.")
                continue

            try:
                if choice == 1:
                    self._add_apartment()
                elif choice == 2:
                    self._show_all()
                elif choice == 3:
                    self._search_menu()
                elif choice == 4:
                    self._filter_menu()
                elif choice == 5:
                    self._sort_menu()
                elif choice == 6:
                    self._rent_apartment()
                elif choice == 7:
                    self._archive_apartment()
                elif choice == 8:
                    self._delete_apartment()
                elif choice == 0:
                    self._save()
                    print("Данные сохранены. Выход из программы.")
                    break
                else:
                    print("Ошибка: такого пункта меню нет.")
            except (ValueError, ApartmentAppError) as error:
                print("Ошибка:", error)

    @staticmethod
    def _print_menu() -> None:
        print()
        print("=== Приложение для аренды недвижимости ===")
        print("1. Добавить квартиру")
        print("2. Показать все квартиры")
        print("3. Поиск")
        print("4. Фильтрация")
        print("5. Сортировка")
        print("6. Сдать квартиру")
        print("7. Архивировать квартиру")
        print("8. Удалить квартиру")
        print("0. Выход")
        print()

    def _add_apartment(self) -> None:
        title = input("Название: ")
        address = input("Адрес: ")
        area = float(input("Площадь: "))
        price = float(input("Цена в месяц: "))
        rent_months = int(input("Срок аренды в месяцах: "))

        apartment = Apartment(
            title=title,
            area=area,
            price=price,
            address=address,
            rent_months=rent_months,
        )

        self._app.add_apartment(apartment)
        print("Квартира добавлена.")

    def _show_all(self) -> None:
        apartments = self._app.get_all()
        self._print_apartments(apartments)

    def _search_menu(self) -> None:
        print("1. По названию")
        print("2. По адресу")

        choice = int(input("Выберите поиск: "))

        if choice == 1:
            title = input("Введите название: ")
            result = self._app.find_by_title(title)
        elif choice == 2:
            address = input("Введите адрес: ")
            result = self._app.find_by_address(address)
        else:
            print("Такого пункта нет.")
            return

        self._print_apartments(result)

    def _filter_menu(self) -> None:
        print("1. По статусу")
        print("2. По диапазону цены")

        choice = int(input("Выберите фильтр: "))

        if choice == 1:
            status = input("Статус available/rented/archived: ")
            result = self._app.filter_by_status(status)
        elif choice == 2:
            min_price = float(input("Минимальная цена: "))
            max_price = float(input("Максимальная цена: "))
            result = self._app.filter_by_price_range(min_price, max_price)
        else:
            print("Такого пункта нет.")
            return

        self._print_apartments(result)

    def _sort_menu(self) -> None:
        print("1. По названию")
        print("2. По цене")
        print("3. По площади")

        choice = int(input("Выберите сортировку: "))

        if choice == 1:
            result = self._app.sort_by_title()
        elif choice == 2:
            result = self._app.sort_by_price()
        elif choice == 3:
            result = self._app.sort_by_area()
        else:
            print("Такого пункта нет.")
            return

        self._print_apartments(result)

    def _rent_apartment(self) -> None:
        self._show_all()
        index = int(input("Введите номер квартиры: ")) - 1
        self._app.rent_apartment(index)
        print("Квартира сдана.")

    def _archive_apartment(self) -> None:
        self._show_all()
        index = int(input("Введите номер квартиры: ")) - 1
        self._app.archive_apartment(index)
        print("Квартира отправлена в архив.")

    def _delete_apartment(self) -> None:
        self._show_all()
        index = int(input("Введите номер квартиры: ")) - 1

        confirm = input("Точно удалить квартиру? да/нет: ")

        if confirm.lower() != "да":
            print("Удаление отменено.")
            return

        deleted = self._app.delete_apartment(index)
        print("Удалено:", deleted)

    def _save(self) -> None:
        save_apartments(
            apartments=self._app.get_all(),
            filepath=self._storage_path,
        )

    @staticmethod
    def _print_apartments(apartments: list[Apartment]) -> None:
        if not apartments:
            print("Список пуст.")
            return

        print()
        print("№ | Название | Площадь | Цена | Адрес | Срок | Статус")
        print("-" * 80)

        for index, apartment in enumerate(apartments, start=1):
            print(f"{index}. {apartment}")