import csv


def get_phones_from_file(file: str) -> list:
    """
    Функция, которая получает на вход имя файла и считывает данные, возвращает список полученных данных.

    :param file: (str) имя передаваемого файла
    :return: list
    """
    with open(f'{file}', 'r') as file:
        raw_data = csv.reader(file)
        data_list = [phone for phone in raw_data]

        return data_list


def unpack_data(data_from_file: list) -> list[str]:
    cleaned_data = []

    for row in data_from_file:
        for data in row:
            cleaned_data.append(data)

    return cleaned_data

file_name = 'test.csv'
data = get_phones_from_file(file_name)
clean_data = unpack_data(data)

print(clean_data)
