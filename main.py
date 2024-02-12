if __name__ == "__main__":
    class StorageDevice:
        """
        Базовый класс, представляющий устройство хранения данных.
        """

        def __init__(self, capacity: int, interface: str):
            """
            Инициализация устройства хранения данных.
            """
            self.capacity = capacity
            self.interface = interface

        def __str__(self) -> str:
            return f"Устройство хранения: {self.capacity}GB, интерфейс {self.interface}"

        def __repr__(self) -> str:
            return f"StorageDevice({self.capacity}, '{self.interface}')"

        def read_data(self) -> str:
            """
            Считывает данные с устройства.
            """
            return "Чтение данных..."

        def write_data(self, data: str) -> str:
            """
            Запись данных на устройство.
            """
            return "Запись данных..."

        def format_data(self) -> str:
            """
            Форматирует устройство.
            """
            return "Форматирование устройства..."


    class SSD(StorageDevice):
        """
        Класс, реализующий SSD
        """

        def __init__(self, capacity: int, interface: str, write_speed: int):
            """
            Расширение конструктора базового класса добавлением скорости записи.

            param write_speed: Скорость записи данных в МБ/с.
            """
            super().__init__(capacity, interface)
            self.write_speed = write_speed

        def write_data(self, data: str) -> str:
            """
            Перегружает метод записи данных для демонстрации способностей SSD к быстрой записи.
            """
            return f"Запись данных на SSD со скоростью {self.write_speed}МБ/с."

        # Наследует метод format_data без изменений.


    class HDD(StorageDevice):
        """
        Класс, реализующий HDD.
        """

        def __init__(self, capacity: int, interface: str, rpm: int):
            """
            Расширение конструктора базового класса добавлением параметра скорости вращения диска.

            :param rpm: Скорость вращения дисков в об/мин.
            """
            super().__init__(capacity, interface)
            self.rpm = rpm

        def read_data(self) -> str:
            """
            Перегружает метод чтения данных, учитывающий скорость вращения диска
            """
            return f"Чтение данных с HDD при скорости вращения {self.rpm} RPM."

        # Наследует метод format_data без изменений.

    pass
