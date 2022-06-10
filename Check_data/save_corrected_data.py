import csv
import os

def get_corrected_numbers(data: set) -> None:
    """
    Получает на вход готовые номера и записывает их в файл.

    :param data: передаются отформатированные номера
    :return: None
    """
    with open('corrected_phones.cvs', 'w', newline='') as file:
        file_saver = csv.writer(file)
        for i_data in data:
            file_saver.writerow([i_data])

