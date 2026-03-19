"""
Модуль генерации статических данных, связанных с людьми.
"""

import csv
import random


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
    for _ in range(1000):
        last_name = random.choice(last_names)
        sex = 'Муж' if last_name[1] == 'M' else 'Жен'
        output_persons.append([last_name[0],
                               random.choice(names[last_name[1]]),
                               random.choice(patronymics[last_name[1]]),
                               sex
                              ])

    with open('output/dict_persons.tsv', 'w', newline='', encoding='utf-8') as file_out:
        tsv_writer = csv.writer(file_out, delimiter='\t', lineterminator='\n')
        tsv_writer.writerows(output_persons)
