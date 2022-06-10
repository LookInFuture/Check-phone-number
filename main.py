from save_corrected_data import get_corrected_numbers
from check_and_handle import cleaned_phones


if __name__ == '__main__':
    try:
        get_corrected_numbers(cleaned_phones)
    except Exception as e:
        print('Не известная ошибка: {}'.format(e))
