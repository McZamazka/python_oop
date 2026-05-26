class ApartmentAppError(Exception):
    """Базовая ошибка приложения."""
    pass


class DuplicateApartmentError(ApartmentAppError):
    """Ошибка при добавлении дубликата квартиры."""
    pass


class ApartmentNotFoundError(ApartmentAppError):
    """Ошибка, если квартира не найдена."""
    pass