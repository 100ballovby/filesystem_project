from pathlib import Path
from os import path


class MyPath:
    """
    Класс для работы с путями в проекте.
    Args:
        path_str: Путь к файлу или папке на компьютере
    Attributes:
        path: Объект pathlib, представляет путь
        is_file: True, если объект является файлом. False - если директорией
        is_dir: True, если объект является директорией. False - если файлом
    """
    def __init__(self, path_str):
        self.path = Path(path_str)
        self.is_file = self.path.is_file()
        self.is_dir = self.path.is_dir()

    def __str__(self):
        """
        Возвращает абсолютный путь к файлу
        """
        return str(self.path.absolute())

    def read_file(self):
        """
        Чтение текста из файла
        :return: Строка текста из файла
        """
        if not self.is_file:  # если параметр is_file = False
            raise ValueError("Невозможно прочитать текст. Передан не текстовый файл.")
        with open(self.path, 'rb') as file:
            return file.read()

    def write_file(self, text):
        """
        Запись текста в файл
        :param text: текст: который нужно записать
        """
        if not self.is_file:
            raise ValueError('Невозможно записать текст. Передан не текстовый файл.')
        with open(self.path, 'w') as f:
            f.write(text)

    def list_dir(self):
        """
        Список содержимого папки
        :return: Список объектов Path, представляющих содержимое папки
        """
        if not self.is_dir:
            raise ValueError('Нельзя получить список содержимого. Передана не папка')
        return list(self.path.iterdir())

    def create_dir(self):
        """
        Создание папки
        :param name: название папки
        """
        if not self.is_exists():
            raise ValueError('Папка уже существует')
        self.path.mkdir(parents=True)

    def delete(self):
        """
        удаление файла или папки
        """
        if self.is_file:
            self.path.unlink()
        elif self.is_dir:
            self.path.rmdir()
        else:
            raise ValueError('Путь не существует')

    def rename(self, new_name):
        """
        Переименовывание файла или папки
        :param new_name: новое имя файла или папки
        """
        if not self.is_exists():
            raise ValueError('Путь не существует')
        self.path.rename(new_name)

    def is_exists(self):
        """
        Проверка существования пути
        :return: True - если переданный путь существует, False - если нет
        """
        return self.path.exists()

    def get_size(self):
        """
        Определение рахмера файла
        :return: размер файла в байтах
        """
        if not self.is_file:
            raise ValueError("Невозможно получить размер файла. Передан не файл.")
        return self.path.stat().st_size

    def get_mtime(self):
        """
        Получение времени последней модификации
        :return: Время последней модификации в формате timestamp
        """
        return self.path.stat().st_mtime

