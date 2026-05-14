from __future__ import annotations

from typing import Callable, Generic, Iterator, Optional, Protocol, TypeVar, runtime_checkable


@runtime_checkable
class Displayable(Protocol):
    def display(self) -> str:
        ...


@runtime_checkable
class Scorable(Protocol):
    def score(self) -> float:
        ...


T = TypeVar("T")
R = TypeVar("R")

D = TypeVar("D", bound=Displayable)
S = TypeVar("S", bound=Scorable)


class TypedCollection(Generic[T]):
    def __init__(self, item_type: type) -> None:
        self._items: list[T] = []
        self._item_type: type = item_type

    def add(self, item: T) -> None:
        if not isinstance(item, self._item_type):
            raise TypeError("Объект не соответствует типу коллекции.")
        self._items.append(item)

    def remove(self, item: T) -> None:
        self._items.remove(item)

    def get_all(self) -> list[T]:
        return list(self._items)

    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        for item in self._items:
            if predicate(item):
                return item
        return None

    def filter(self, predicate: Callable[[T], bool]) -> "TypedCollection[T]":
        result: TypedCollection[T] = TypedCollection(self._item_type)

        for item in self._items:
            if predicate(item):
                result.add(item)

        return result

    def map(self, transform: Callable[[T], R]) -> list[R]:
        return [transform(item) for item in self._items]

    def __iter__(self) -> Iterator[T]:
        return iter(self._items)

    def __len__(self) -> int:
        return len(self._items)

    def __getitem__(self, index: int) -> T:
        return self._items[index]