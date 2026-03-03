"""
Основной модуль приложения.
"""

import os
from dictionaries import persons


def main():
    """
    Точка входа приложения.
    """

    # Проверяем наличие и создаем директорию output для вывода
    if not os.path.isdir('output'):
        os.mkdir('output')

    persons.persons()


if __name__ == '__main__':
    main()
