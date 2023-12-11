import doctest
from typing import List

"""
Функционал приложения для симуляции игрового процесса
Объекты: Игрок, оружие, игровой мир
"""


class Player:
    """Класс, описывающий игрока."""
    level: int

    def __init__(self, name: str, level: int, experience: int):
        """
        Создание объекта "Игрок"
        :param name: Имя игрока
        :param level: игровой уровень игрока
        :param experience: игровой опыт  игрока

        Уровень персонажа и опыт проверяется на валидность,
        так как не может быть отрицательным.
        Также создается пустое множество оружий данного персонажа.

        Примеры:
        >>> player1 = Player("Python Player", 10, 100) # инициализация экземпляра класса
        """
        self.name = name

        if level < 0:
            raise ValueError("Уровень не может быть отрицательным")
        self.level = level

        if experience < 0:
            raise ValueError("Опыт не может быть отрицательным")
        self.experience = experience

        # инвентарь оружия игрока
        self.weapons = set()

    def level_up(self) -> None:
        """
        Перевод игрока с одного уровня на другой(Повышение уровня, понизить уровень нельзя)

        Примеры:
        >>> player1 = Player("Python Player", 10, 100)
        >>> player1.level_up() #Повысился уровень сложности
        """
        self.level += 1

    def earn_experience(self, exp: int) -> None:
        """
        Добавить игроку очки опыта. Отобрать нельзя, лишь дать 0 или больше очков.
        :param exp: Опыт
        Примеры:
        >>> player1 = Player("Python Player", 10, 100)
        >>> player1.earn_experience(100) #Повысился уровень сложности
        """
        if exp < 0:
            raise ValueError("Опыт не может быть отрицательным")
        self.experience += exp

    def get_level(self) -> int:
        """
        Получение уровня игрока
        :return: уровень игрока
        :rtype: int
        Примеры:
        >>> player1 = Player("Python Player", 10, 100)
        >>> level = player1.get_level() # получение уровня
        """
        return self.level

    def get_experience(self) -> int:
        """
        Получение опыта игрока
        :return: опыт игрока
        :rtype: int
        Примеры:
        >>> player1 = Player("Python Player", 10, 100)
        >>> level = player1.get_experience() # получение уровня
        """
        return self.experience

    def add_weapon(self, weapon: 'Weapon') -> None:
        """
                Добавление оружия герою
                :param weapon: Оружие
                Примеры:
                >>> player1 = Player("Python Player", 10, 100)
                >>> weapon = Weapon("Knife", 15, 2)
                >>> player1.add_weapon(weapon) # добавление weapon игроку
                """
        if not isinstance(weapon, Weapon):
            raise TypeError("Оружие может быть только объект класса \"Оружие\"")
        ...


class Weapon:
    """
    Сущность оружия
    """

    def __init__(self, name: str, damage: int, speed_attack: int):
        """
        Создание и подготовка к работе объекта "Оружие"
        :param name: Название оружия
        :param damage: Количество урона
        :param speed_attack: Скорость атаки данного оружия
        Примеры:
        >>> weapon1 = Weapon("Knife",15 , 2)
        >>> weapon2 = Weapon("Pistol", 50, 10)
        """
        self.name = name
        if damage <= 0:
            raise ValueError("Damage должен быть положительным")
        self.damage = damage
        if speed_attack <= 0:
            raise ValueError("Скорость аттаки должна быть положительная")
        self.speed_attack = speed_attack

    def upgrade_damage(self, diff_damage: int) -> None:
        """
        Улучшение урона оружия
        :param diff_damage: Количество единиц силы, на сколько увеличился дамаг,
        не может быть отрицательным
        Примеры:
        >>> weapon3 = Weapon("Knife",15 , 2)
        >>> weapon3.upgrade_damage(15)
        """
        if diff_damage < 0:
            raise ValueError("Нельзя убавить Damage оружия")
        ...

    def upgrade_speed(self, diff_speed: int) -> None:
        """
        Улучшение скорости оружия
        :param diff_speed: Количество единиц, на сколько увеличилась скорость,
        не может быть отрицательным
        Примеры:
        >>> weapon3 = Weapon("Knife",15 , 2)
        >>> weapon3.upgrade_speed(15)
        """
        if diff_speed < 0:
            raise ValueError("Нельзя убавить скорость оружия")
        ...


class GameWorld:
    """
    Класс, описывающий игровой мир.

    Attributes:
        world_name (str): Название игрового мира.
        locations (List[str]): Список доступных локаций в мире.

    Methods:
        explore_location(self, location: str) -> None:
            Исследовать указанную локацию в игровом мире.


        complete_quest(self, quest_name: str) -> bool:
            Завершить указанное задание в игровом мире.

    """

    def __init__(self, world_name: str, locations: List[str]):
        """
        Создание и подготовка игрового мира
        :param world_name: Название мира
        :param locations: Список его локаций
        Примеры:
        >>> game_world = GameWorld("C++", ["Class","template","auto","Python"])
       """
        self.world_name = world_name
        self.locations = locations

    def explore_location(self, location: str) -> None:
        """
        Метод изучения локации(как новой, так и старой)

        :param location: название локации
        При этом локация может быть как уже в locations, так и отстутствовать в нем
        Примеры:
        >>> game_world = GameWorld("C++", ["Class","template","auto","Python"])
        >>> game_world.explore_location("Java")
        """
        ...

    def complete_quest(self, quest_name: str) -> bool:
        """
        Возвращает состояние: получилось ли пройти данное задание или нет

        :return: Состояние (прошел или нет)
        :rtype: bool

        Примеры:
        >>> game_world = GameWorld("C++", ["Class","template","auto","Python"])
        >>> game_world.complete_quest("Save bank account")
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # работоспособность экземпляров класса проверить с помощью doctest
