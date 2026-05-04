from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def display(self):
        pass


class Calculable(ABC):
    @abstractmethod
    def calculate_income(self):
        pass