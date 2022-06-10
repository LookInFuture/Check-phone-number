from typing import Set
from get_file_from_system import clean_data


def check_if_startswith8(data: list) -> Set[str]:
    """
    Функция заменяет все номера, которые начинаются на 8 на 7.

    :param data: список номеров
    :return: set всех номеров, включая скорректированные
    """

    cleaned_data = set()
    for phone in clean_data:
        if phone.startswith('8'):
            phone_list = list(phone)
            phone_list[0] = '7'
            new_phone = ''.join(phone_list)
            cleaned_data.add(new_phone)
            continue
        cleaned_data.add(phone)

    return cleaned_data


def check_if_only_digits(data_set: set) -> Set[str]:
    """
    Проверяет, чтобы в номера входили только цифры.

    :param data_set: Список номеров с разными символами
    :return: Список номеров только с цифрами
    """
    corrected_phone = set()
    for data in data_set:
        phone_wo_symbols = []
        for i_sym in data:
            if i_sym.isnumeric():
                phone_wo_symbols.append(i_sym)

        if len(phone_wo_symbols) == 11:
            new_phone = ''.join(phone_wo_symbols)
            corrected_phone.add(new_phone)

    return corrected_phone


set_clean_data = check_if_startswith8(clean_data)
cleaned_phones = check_if_only_digits(set_clean_data)
