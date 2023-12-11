# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Box:
    def __init__(self, material: str, volume: float):
        """
        Инициализация коробки.
        :param material: материал изготовления.
        :param volume: объем коробки.
        Примеры:
        >>> box = Box("Картон", 2.2)
        """
        if not isinstance(material, str):
            raise TypeError("Материал должен задаваться строкой")
        if not isinstance(volume, float) or volume < 0.0:
            raise ValueError("Объем должен быть представлен положительным вещественным числом")
        self.material = material
        self.volume = volume

    def addItem(self, item: str):
        """
        Добавляет что-то в коробку
        :param item: предмет, добавленный в коробку.
        Примеры:
        >>> box = Box("Картон", 2.2)
        >>> box.addItem("Диско-шар")
        """
        ...

    def removeItem(self, item: str):
        """
        Удаляет предмет из коробки.
        :param item: предмет из коробки.
        Примеры:
        >>> box = Box("Картон", 2.2)
        >>> box.removeItem("Диско-шар")
        """
        ...


class Hammock:
    def __init__(self, size: str, height: float):
        """
        Инициализация гамака.
        :param size: Размер гамака.
        :param height: Высота, на которой он подвешен.
        Примеры:
        >>> hammock = Hammock("Одноместный", 1.1)
        """
        if not isinstance(size, str):
            raise TypeError("Размер должен быть представлен строкой")
        if not isinstance(height, float) or height < 0.0:
            raise ValueError("Высота должен быть представлена положительным вещественным числом")
        self.size = size
        self.height = height

    def hangHammock(self):
        """
        Подвесить гамак.
        Примеры:
        >>> hammock = Hammock("Одноместный", 1.1)
        >>> hammock.hangHammock()
        """
        ...

    def changeWidth(self, width: float):
        """
        Поменять ширину гамака.
        :param width: ширина гамака.
        Примеры:
        >>> hammock = Hammock("Одноместный", 1.1)
        >>> hammock.changeWidth(2.1)
        """
        ...


class Stopwatch:
    def __init__(self, model: str, isWorking: bool):
        """
        Инициализация секундомера.
        :param model: модель часов.
        :param isWorking: рабочий ли секундомер.
        Примеры:
        >>> stopwatch = Stopwatch("model 30-30", True)
        """
        if not isinstance(model, str):
            raise TypeError("Модель часов должна быть представлена строкой")
        if not isinstance(isWorking, bool):
            raise TypeError("Работоспособность должна быть логическим значением")
        self.model = model
        self.isWorking = isWorking

    def setTime(self, hours: int, minutes: int, seconds: int):
        """
        Устанавливает отображаемое значение на секундомере.
        :param hours: Часы.
        :param minutes: Минуты.
        :param seconds: Секунды.
        Примеры:
        >>> stopwatch = Stopwatch("model 30-30", True)
        >>> stopwatch.setTime(0, 0, 0)
        """
        if not isinstance(hours, int) or not (0 <= hours < 24):
            raise ValueError("Часы должны быть представлены целым числом от 0 до 23")
        if not isinstance(minutes, int) or not (0 <= minutes < 60):
            raise ValueError("Минуты должны быть представлены целым числом от 0 до 59")
        if not isinstance(seconds, int) or not (0 <= seconds < 60):
            raise ValueError("Секунды должны быть представлены целым числом от 0 до 59")
        ...

    def pressButton(self):
        """
        нажать на кнопку секундомера.
        Примеры:
        >>> stopwatch = Stopwatch("model 30-30", True)
        >>> stopwatch.pressButton()
        """
        ...

if __name__ == "__main__":
    doctest.testmod()
    pass
