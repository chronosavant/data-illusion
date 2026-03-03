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

    output_persons = []
    for _ in range(1000):
        output_persons.append(random.choice(last_names))

    with open('output/dict_persons.tsv', 'w', newline='', encoding='utf-8') as file_out:
        tsv_writer = csv.writer(file_out, delimiter='\t', lineterminator='\n')
        tsv_writer.writerows(output_persons)
