import csv

from typing import List


def get_phones_from_file(file: str) -> List:
    """
    Функция, которая получает на вход имя файла и считывает данные, возвращает список полученных данных.

    :param file: (str) имя передаваемого файла
    :return: list
    """
    with open(f'{file}', 'r') as file:
        raw_data = csv.reader(file)
        data_list = [phone for phone in raw_data]

        return data_list


def unpack_data(data_from_file: list) -> List[str]:
    """
    Принимает на вход список нормеров и объединяет в один список.

    :param data_from_file: Список списков номеров
    :return: Единый список номеров
    """
    cleaned_data = []

    for row in data_from_file:
        for i_data in row:
            cleaned_data.append(i_data)

    return cleaned_data


file_name = 'Buyers.csv'

data = get_phones_from_file(file_name)
clean_data = unpack_data(data)
