"""
Идея: Реализация иерархии классов на примере сущностей "Автомобили".
Суперкласс: Car
Подклассы: PassengerСar, Truck
"""""


class Car:
    """Базовый класс Car.
    Он хранит общую информацию, а также общую логику перемещения
    (такие как проверка максимальной скорости, ее обновление,
    Цвет, марка и т.д.)"""

    def __init__(self, brand: str, max_speed: float | int, color: str):
        """Инкапсуляция полей нужна для валидности данных. Ибо текущая скорость не может быть
        больше максимальной. Мы можем менять максимальную скорость
        а текущую только изменять"""
        """ Инкапсуляция для  brand необходима, так как brand не должен меняться
        с начала создания машины"""
        if self.max_speed_check(max_speed):
            self.max_speed = max_speed
        if self.string_check(brand):
            self.brand = brand
        if self.string_check(color):
            self.color = color
        self.current_speed = 0

    def start_engine(self) -> None:
        """метод для запуска двигателя."""
        ...

    @staticmethod
    def max_speed_check(value: float | int) -> bool:
        """Метод валидации значения максимальной скорости"""

        if value <= 0:
            raise ValueError("Максимальная скорость должна быть числом")
        return True

    def diff_for_current_speed_check(self, diff: float | int) -> bool:
        """Метод валидации значения  для изменения текущей скорости"""
        if diff + self.current_speed < 0 or diff + self.current_speed > self.max_speed:
            raise ValueError("значение для изменения скорости выходит за рамки возможного")
        return True

    @staticmethod
    def string_check(value: str) -> bool:
        """Метод проверки строки на непустоту"""
        if value is None or value == '':
            raise ValueError("Строка не должна быть пустой")
        return True

    @property
    def max_speed(self) -> (float, int):
        """Getter максимальной скорости, возращает float or int"""
        return self.max_speed

    @max_speed.setter
    def max_speed(self, new_max_speed: int | float) -> None:
        """Setter Максимальной скорости, проверяем на валидность данные
         а потом в случае логической ошибки(текущая скорость больше максимальной),
         меняем текущуб скорость"""
        if self.max_speed_check(new_max_speed):
            self.max_speed = new_max_speed
            if self.max_speed < self.current_speed:
                self.current_speed = self.max_speed

    @property
    def current_speed(self) -> (float, int):
        """Getter текущей скорости"""
        return self.current_speed

    def update_current_speed(self, diff: int | float) -> None:
        """ Метод, который управляет скоростью """
        if self.diff_for_current_speed_check(diff):
            self.current_speed += diff

    @property
    def brand(self) -> str:
        """Getter бренда"""
        return self.brand

    @property
    def color(self) -> str:
        """Getter цвета"""
        return self.color

    @color.setter
    def color(self, new_color: str) -> None:
        """Setter цвета"""
        if self.string_check(new_color):
            self.color = new_color

    def __str__(self) -> str:
        return f"Бренд машины: {self.max_speed}. Достигает максимальную скорость: {self.max_speed}. " \
               f"Цвет:{self.color}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(brand={self.brand!r}, max_speed={self.max_speed!r}, color={self.color})"


class PassengerCar(Car):
    """ Дочерний класс, наследуется от базового класса Car,
    имеет отличительное состояние: number_of_seats - количество мест, а также имеет свои методы
     посадить человека, высадить, изменить количество пассажирских мест"""

    def __init__(self, brand: str, max_speed: (float, int), color: str, number_of_seats: int):
        super().__init__(brand, max_speed, color)
        if self.number_of_seats_check(number_of_seats):
            self.number_of_seats = number_of_seats
        """Количество свободных мест на 1 меньше, т.к. одно место для водителя """
        self.number_of_seats_for_passengers = self.number_of_seats - 1

    @staticmethod
    def number_of_seats_check(number_of_seats) -> bool:
        """Метод валидации значения количества посадочных мест"""
        if not isinstance(number_of_seats, int):
            raise TypeError("Максимальное число мест должно быть числом")
        if number_of_seats <= 0 or number_of_seats >= 7:
            raise ValueError("Некорректное значение максималнього числа мест")
        return True

    def seat_passenger(self) -> None:
        """Метод для посадки людей
        Проверяет наличие свободных мест"""
        if not self.number_of_seats_for_passengers - 1 >= 0:
            raise ValueError("Машина переполнена")
        self.number_of_seats_for_passengers -= 1

    def drop_off_a_passenger(self) -> None:
        """Метод для высадки людей
                Проверяет наличие людей"""
        if self.number_of_seats_for_passengers + 1 >= self.number_of_seats:
            raise ValueError("Салон пустой")
        self.number_of_seats_for_passengers += 1

    def start_engine(self) -> None:
        """Переопределение метода базового класса, Легковые машины будут по-своему стартовать"""
        ...

    @property
    def number_of_seats(self) -> int:
        """Getter для количества мест"""
        return self.number_of_seats

    @property
    def number_of_seats_for_passengers(self) -> int:
        """Getter для количества мест для пассажиров"""
        return self.number_of_seats_for_passengers

    def __str__(self) -> str:
        """Метод __str()__ переопределяется, так как необходимо показать уникальные значеня
        объекта, а именно количество пассажирских мест (на единицу меньше, так как одно сидение для водителя)"""
        parent_string = super().__str__()
        return f"{parent_string} Кол-во пассажирских мест: {self.number_of_seats - 1}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(brand={self.brand!r}, max_speed={self.max_speed!r}, color={self.color}, " \
               f"number_of_seats={self.number_of_seats})"


class Track(Car):
    """ Дочерний класс, наследуется от базового класса Car,
        имеет отличительное состояние: max_load_capacity - количество свободного места для загрузки багажа
        можно загрузить и выгрузить с проверкой на валидность"""

    def __init__(self, brand: str, max_speed: float | int, color: str, max_load_capacity: float | int):
        super().__init__(brand, max_speed, color)
        if self.max_load_capacity_check(max_load_capacity):
            self.max_load_capacity = max_load_capacity
            """Количество свободного места"""
        self.free_places = self.max_load_capacity

    @staticmethod
    def max_load_capacity_check(value) -> bool:
        """ Валидатор свободного места"""
        if not isinstance(value, (float, int)):
            raise TypeError("Максимальная погрузка должна быть числом")
        if value <= 0:
            raise ValueError("Некорректное значение для максимального багажа")
        return True

    def start_engine(self) -> None:
        """Переопределение метода, Грузовые машины будут по-своему стартовать"""
        ...

    @property
    def max_load_capacity(self) -> float | int:
        """Getter максимального размера для багажа"""
        return self.max_load_capacity

    @property
    def free_places(self) -> float | int:
        """Getter свободного места"""
        return self.free_places

    @max_load_capacity.setter
    def max_load_capacity(self, value: float | int) -> None:
        """Setter с валидатором на объем, количество не должно уменьшаться"""
        if value <= 0 or value < self.free_places:
            raise ValueError("Неразрешимое число для максимального значения  capacity")
        self.max_load_capacity = value

    def load_car(self, weight: float | int) -> None:
        """ Уникальный метод для класса -  загрузка машины"""
        if self.free_places - weight < 0:
            raise ValueError("Машина слишком загружена")
        self.free_places -= weight

    def free_car(self, weight: float | int) -> None:
        """ Уникальный метод для класса - освобождение машины"""
        ...

    def __str__(self) -> str:
        """Метод __str()__ переопределяется, так как необходимо показать уникальные значеня
        объекта, а именно количество объема ("""
        parent_string = super().__str__()
        return f"{parent_string} Кол-во объема для загрузки: {self.max_load_capacity}."

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}(brand={self.brand!r}, max_speed={self.max_speed!r}, "
                f"color={self.color!r}, max_load_capacity={self.max_load_capacity!r})")
