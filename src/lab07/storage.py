import json
from models import Apartment


def save_apartments(apartments: list[Apartment], filepath: str) -> None:
    """Сохраняет список квартир в JSON-файл."""
    data = [apartment.to_dict() for apartment in apartments]

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def load_apartments(filepath: str) -> list[Apartment]:
    """Загружает список квартир из JSON-файла."""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        return []

    return [Apartment.from_dict(item) for item in data]