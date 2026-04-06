"""
Модуль генерации статических данных, связанных с людьми.
"""

import csv
import random
from datetime import datetime, timedelta


def persons():
    """
    Генерация статического справочника людей.
    """

    with open('data/last_names.tsv', 'r', newline='', encoding='utf-8') as file_in:
        tsv_reader = csv.reader(file_in, delimiter='\t')
        last_names = list(tsv_reader)

    names = { 'M': [], 'F': []}
    with open('data/names.tsv', 'r', newline='', encoding='utf-8') as file_in:
        tsv_reader = csv.reader(file_in, delimiter='\t')
        for name, sex in tsv_reader:
            names[sex].append(name)

    patronymics = { 'M': [], 'F': []}
    with open('data/patronymics.tsv', 'r', newline='', encoding='utf-8') as file_in:
        tsv_reader = csv.reader(file_in, delimiter='\t')
        for patronymic, sex in tsv_reader:
            patronymics[sex].append(patronymic)

    output_persons = []
    id_autoincrement = 0
    for _ in range(1000):
        last_name = random.choice(last_names)
        sex = 'Муж' if last_name[1] == 'M' else 'Жен'
        # Дата рождения выбирается из диапазона от 14 до 90 лет с момента генерации
        birth_date = datetime.now() - timedelta(days=random.randint(5114, 32873))
        id_autoincrement = id_autoincrement + 1
        output_persons.append([id_autoincrement,
                               last_name[0],
                               random.choice(names[last_name[1]]),
                               random.choice(patronymics[last_name[1]]),
                               sex,
                               birth_date.strftime('%Y-%m-%d')
                              ])

    with open('output/dict_persons.tsv', 'w', newline='', encoding='utf-8') as file_out:
        tsv_writer = csv.writer(file_out, delimiter='\t', lineterminator='\n')
        tsv_writer.writerows(output_persons)
