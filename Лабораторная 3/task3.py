class Book:
    """ Базовый класс книги """

    def __init__(self, name: str, author: str):
        """ Поля  name  и author  не изменяются. У них есть только Getter"""
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга: {self._name}. Автор: {self._author}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author


class PaperBook(Book):
    """ Бумажная книга """
    """Наследуется от базового класса Book"""

    def __init__(self, name: str, author: str, pages: int):
        """ Поле pages не изменяется """
        super().__init__(name, author)
        if self.pages_check(pages):
            self._pages = pages

    def __str__(self):
        parent_string = super().__str__()
        return f"{parent_string} Кол-во страниц: {self.pages}."

    def __repr__(self):
        """ Могут быть унаследованы, когда меняется поведение(добавляются методы и т.д.),
            но когда меняются состояния, мы обязаны __str__ & __repr__ перегрузить """
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages})"

    @property
    def pages(self) -> int:
        return self._pages

    @staticmethod
    def pages_check(value) -> bool:
        """Метод валидации значения кол-ва страниц книги"""
        if not isinstance(value, int):
            raise TypeError("Количество страниц книги должно быть целым числом.")
        if value <= 0:
            raise ValueError("Количество страниц книги должно быть положителным числом.")
        return True


class AudioBook(Book):
    """ Аудиокнига """
    """ Наследуется от базового класса Book """

    def __init__(self, name: str, author: str, duration: int | float):
        """ Поле duration не изменяется.
        Происходит проверка типа(т.к. должно быть или int или float),
        а также проверка на смысл данных(не может быть неположительным числом)
        """
        super().__init__(name, author)
        if self.duration_check(duration):
            self._duration = duration

    def __str__(self):
        parent_string = super().__str__()
        return f"{parent_string} Продолжительность: {self.duration}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration})"

    @property
    def duration(self) -> int | float:
        return self._duration

    @staticmethod
    def duration_check(value) -> bool:
        """Метод валидации значения duration"""
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность  должна быть целым или дробным числом.")
        if value <= 0:
            raise ValueError("Продолжительность  должна быть положительным числом.")
        return True


if __name__ == '__main__':
    """Создание разных экземпляров класса и проверка методов"""

    book = Book("Что делать?", "Н.Г.Чернышевский")
    paper_book = PaperBook(book.name, book.author, 812)

    """Проверка наследования"""
    audio_book = AudioBook(paper_book.name, paper_book.author, 52.7)

    multi_library = [paper_book, audio_book]

    for obj in multi_library:
        print(f"\n{obj.__class__}")
        print(f"__str__: {str(obj)}")
        print(f"__repr__: {repr(obj)}")
        print(f"'name': {obj.name}")
        print(f"'author': {obj.author}")

        if isinstance(obj, PaperBook):
            print(f"'pages': {obj.pages}")
        if isinstance(obj, AudioBook):
            print(f"'duration': {obj.duration}")
        print('\n')

    print("================= Invalid argument's  tests")

    """Тест на целочисленность страниц книг"""
    try:
        paper_error_book = PaperBook("float test", "for Paper book", 2.5)
    except TypeError as e:
        print(e)

    try:
        """Тест на положительное значение времени аудиокниги"""
        audio_error_book = AudioBook("negative test", "for audio book", -55)
    except ValueError as e:
        print(e)

    print("\n=======Test to change value for books")
    try:
        paper_book.name = "Another name"
    except Exception as e:
        print(e)
