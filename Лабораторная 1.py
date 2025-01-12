# TODO Написать 3 класса с документацией и аннотацией типов
from abc import ABC, abstractmethod


class Furniture(ABC):
    """
    Абстрактный класс для описания мебели.

    Атрибуты:
        material (str): Материал, из которого сделана мебель.
        dimensions (tuple): Размеры мебели (длина, ширина, высота).
    """

    def __init__(self, material: str, dimensions: tuple):
        if not material:
            raise ValueError("Материал не может быть пустым.")
        if len(dimensions) != 3 or not all(isinstance(dim, (int, float)) and dim > 0 for dim in dimensions):
            raise ValueError("Размеры должны быть положительными числами и содержать 3 элемента.")

        self.material = material
        self.dimensions = dimensions

    @abstractmethod
    def assemble(self) -> None:
        """
        Метод для сборки мебели.
        """
        ...

    @abstractmethod
    def move(self, new_location: str) -> None:
        """
        Метод для перемещения мебели.

        Args:
            new_location (str): Новое местоположение мебели.
        """
        ...


class Tree(ABC):
    """
    Абстрактный класс для описания дерева.

    Атрибуты:
        species (str): Вид дерева.
        age (int): Возраст дерева.
    """

    def __init__(self, species: str, age: int):
        if not species:
            raise ValueError("Вид дерева не может быть пустым.")
        if age < 0:
            raise ValueError("Возраст дерева должен быть положительным.")

        self.species = species
        self.age = age

    @abstractmethod
    def photosynthesize(self) -> None:
        """
        Метод для процесса фотосинтеза.
        """
        ...

    @abstractmethod
    def grow(self, years: int) -> None:
        """
        Метод для роста дерева.

        Args:
            years (int): Количество лет, на которое дерево выросло.
        """
        ...


class SocialMedia(ABC):
    """
    Абстрактный класс для описания социальной сети.

    Атрибуты:
        name (str): Название социальной сети.
        active_users (int): Количество активных пользователей.
    """

    def __init__(self, name: str, active_users: int):
        if not name:
            raise ValueError("Название социальной сети не может быть пустым.")
        if active_users < 0:
            raise ValueError("Количество пользователей должно быть положительным.")

        self.name = name
        self.active_users = active_users

    @abstractmethod
    def post(self, content: str) -> None:
        """
        Метод для публикации контента.

        Args:
            content (str): Текст публикации.
        """
        ...

    @abstractmethod
    def add_user(self) -> None:
        """
        Метод для добавления нового пользователя.
        """
        ...
if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
      import doctest
      doctest.testmod()
