from pathlib import Path
import os

# Tasks:
# |X| Add func check dir, if not - create dir
# |X| Create own packet with pip


TYPE_FILE = '.py'

MAIN_FOLDERS = {
    0: 'Modul',
}


TYPES = {
    0: 'note',
    1: 'theory',
    2: 'practice',
    3: 'you_theory',
    4: 'you_practice',
    5: 'you_add',
    6: 'autocheck',
    7: 'own_exe',
    8: 'chekio'
}


FOLDERS = {
    0: '0_Notes',
    1: '1_Theory',
    2: '2_Practice',
    3: '3_Youtube_theory',
    4: '4_Youtube_practice',
    5: '5_Youtube_add',
    6: '6_Autocheck',
    7: '7_Own_exersice',
    8: '8_Chekio'
}


def enter_number_of_modul():

    while True:
        try:
            user_input = input('Enter number of Modul: ')
            break
        except TypeError:
            print('Wrong number. Try again')

    return user_input


def choose_type():

    for key, type in TYPES.items():
        print(f'{key} - {type}')

    while True:
        try:
            user_input = int(input('Choose type of file: '))
            break
        except TypeError:
            print('Wrong number. Try again')

    return user_input


def get_parent_folder():

    # my_path = os.path.abspath(__file__ + '\..')
    path = Path()
    # my_path = Path(my_path)

    # return my_path
    return path


def get_number_next_file_in_folder(path):
    number = 1

    for _ in path.iterdir():
        number += 1

    return number


def enter_explanation_of_file():

    while True:
        try:
            user_input = input('Enter the short explanation of file: ').split()
            user_input = '_'.join(user_input)
            break
        except TypeError:
            print('Something wrong. Try again')

    return user_input


def normal_number(number: str) -> str:
    return f'{number}' if int(number) > 9 else f'0{number}'


def main():

    # Отриммуємо шлях до папки де треба зробити шаблон
    my_path = get_parent_folder()

    # Отримуємо необхідну інформацію від користувача
    user_input_modul = normal_number(enter_number_of_modul())
    user_input_type = choose_type()
    user_input_explanation = enter_explanation_of_file()


    folder_name = '_'.join(('Modul', user_input_modul))
    
    # Створюємо папку, якщо її не існує
    path_with_folder = Path(f'{my_path}\{folder_name}\{FOLDERS[user_input_type]}')
    path_with_folder.mkdir(parents=True, exist_ok=True) 

    # Отримуємо кількість файлів в папці, щоб присвоїти номер наступного файлу
    next_number_file = normal_number(get_number_next_file_in_folder(path_with_folder))

    file_name = '_'.join((user_input_modul, 
                      TYPES[user_input_type], 
                      str(next_number_file), 
                      user_input_explanation,
                      TYPE_FILE))
    
    path_of_new_file = Path(f'{path_with_folder}\{file_name}')

    with open(path_of_new_file, 'w') as file:
        
        print(f'------\nFile created: {file_name}.\nPath: {path_of_new_file}\n------')


if __name__ == '__main__':

    main()