def validate_title(value):
    if not isinstance(value, str):
        raise TypeError("Название должно быть строкой.")
    if not value.strip():
        raise ValueError("Название не может быть пустым.")
    return value.strip()


def validate_area(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Площадь должна быть числом.")
    if value <= 0:
        raise ValueError("Площадь должна быть больше 0.")
    return float(value)


def validate_price(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Цена должна быть числом.")
    if value <= 0:
        raise ValueError("Цена должна быть больше 0.")
    return float(value)


def validate_address(value):
    if not isinstance(value, str):
        raise TypeError("Адрес должен быть строкой.")
    if not value.strip():
        raise ValueError("Адрес не может быть пустым.")
    return value.strip()


def validate_rent_months(value):
    if not isinstance(value, int):
        raise TypeError("Срок аренды должен быть целым числом.")
    if value <= 0:
        raise ValueError("Срок аренды должен быть больше 0.")
    return value


def validate_status(value):
    if not isinstance(value, str):
        raise TypeError("Статус должен быть строкой.")

    allowed_statuses = {"available", "rented", "archived"}
    if value not in allowed_statuses:
        raise ValueError(
            f"Недопустимый статус: {value}. Разрешены: {', '.join(allowed_statuses)}."
        )
    return value