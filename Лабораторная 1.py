
from abc import ABC, abstractmethod
from typing import List, Tuple, Optional
import doctest

class Book(ABC):
    """
    Абстрактный класс, представляющий книгу.

    Атрибуты:
        id (int): Идентификатор книги.
        name (str): Название книги.
        pages (int): Количество страниц в книге.
    
    Примеры:
         >>> class ConcreteBook(Book):
         ...     def __init__(self, id_, name, pages):
         ...         super().__init__(id_, name, pages)
         >>> book = ConcreteBook(id_=1, name='test_name', pages=200)
    """

    def __init__(self, id_: int, name: str, pages: int):
        if not isinstance(id_, int) or id_ <= 0:
            raise ValueError("ID книги должно быть целым положительным числом.")
        if not isinstance(name, str) or not name:
            raise ValueError("Название книги должно быть не пустой строкой.")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть целым положительным числом.")

        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """
        Возвращает строку в формате "Книга \"название_книги\"".
        
        Примеры:
            >>> class ConcreteBook(Book):
            ...     def __init__(self, id_, name, pages):
            ...         super().__init__(id_, name, pages)
            >>> book = ConcreteBook(id_=1, name='test_name', pages=200)
            >>> print(book)
            Книга "test_name"
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Возвращает валидную python строку для инициализации экземпляра Book.
        
        Примеры:
            >>> class ConcreteBook(Book):
            ...     def __init__(self, id_, name, pages):
            ...         super().__init__(id_, name, pages)
            >>> book = ConcreteBook(id_=1, name='test_name', pages=200)
            >>> repr(book)
            "Book(id_=1, name='test_name', pages=200)"
        """
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


class Library:
    """
    Класс, представляющий библиотеку книг.

    Атрибуты:
        books (list[Book]): Список книг в библиотеке.
    
     Примеры:
        >>> class ConcreteBook(Book):
        ...     def __init__(self, id_, name, pages):
        ...         super().__init__(id_, name, pages)
        >>> book1 = ConcreteBook(id_=1, name='test_name_1', pages=200)
        >>> book2 = ConcreteBook(id_=2, name='test_name_2', pages=400)
        >>> library = Library(books=[book1, book2])
    """
    def __init__(self, books: list[Book] = None):
      if books is None:
        self.books = []
      else:
        if not isinstance(books, list):
          raise ValueError("Аргумент books должен быть списком")
        for book in books:
          if not isinstance(book, Book):
             raise ValueError("Список книг должен содержать экземпляры класса Book")
        self.books = books

    def get_next_book_id(self) -> int:
        """
        Возвращает идентификатор для новой книги.
        Если книг в библиотеке нет, то вернуть 1.
        Если книги есть, то вернуть идентификатор последней книги увеличенный на 1.
        
         Примеры:
            >>> class ConcreteBook(Book):
            ...     def __init__(self, id_, name, pages):
            ...         super().__init__(id_, name, pages)
            >>> book1 = ConcreteBook(id_=1, name='test_name_1', pages=200)
            >>> book2 = ConcreteBook(id_=2, name='test_name_2', pages=400)
            >>> library = Library(books=[book1, book2])
            >>> library.get_next_book_id()
            3
            >>> empty_library = Library()
            >>> empty_library.get_next_book_id()
            1
        """
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Возвращает индекс книги в списке по ее ID.
        Если книга существует, то вернуть индекс из списка.
        Если книги нет, то вызвать ошибку ValueError с сообщением: "Книги с запрашиваемым id не существует".
        
         Примеры:
            >>> class ConcreteBook(Book):
            ...     def __init__(self, id_, name, pages):
            ...         super().__init__(id_, name, pages)
            >>> book1 = ConcreteBook(id_=1, name='test_name_1', pages=200)
            >>> book2 = ConcreteBook(id_=2, name='test_name_2', pages=400)
            >>> library = Library(books=[book1, book2])
            >>> library.get_index_by_book_id(2)
            1
            >>> try:
            ...   library.get_index_by_book_id(3)
            ... except ValueError as e:
            ...    print(e)
            Книги с запрашиваемым id не существует
        """
        if not isinstance(book_id, int) or book_id <= 0:
            raise ValueError("ID книги должно быть целым положительным числом.")
        for index, book in enumerate(self.books):
          if book.id == book_id:
            return index
        raise ValueError("Книги с запрашиваемым id не существует")

if __name__ == '__main__':
    doctest.testmod()
    # инициализируем список книг
     list_books = [
   Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
     ]
     for book in list_books:
         print(book)  # проверяем метод str

     print(list_books)  # проверяем метод repr

    # # проверяем работоспособность методов класса Library
    # library = Library(list_books)
    # print(f"Следующий id книги: {library.get_next_book_id()}")

    # try:
    #   book_index = library.get_index_by_book_id(2)
    #   print(f"Индекс книги с ID=2: {book_index}")
    #   book_index = library.get_index_by_book_id(3)
    #   print(f"Индекс книги с ID=3: {book_index}")
    # except ValueError as e:
    #   print(f"Произошла ошибка: {e}")

    # empty_library = Library()
    # print(f"Следующий id книги в пустой библиотеке: {empty_library.get_next_book_id()}")
