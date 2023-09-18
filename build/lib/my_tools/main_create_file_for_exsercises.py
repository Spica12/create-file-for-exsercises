from pathlib import Path
import os

# Tasks:
# | | Add func check dir, if not - create dir
# | | Create own packet with pip


TYPE_FILE = '.py'


TYPES = {
    1: 'theory',
    2: 'practice',
    3: 'you_theory',
    4: 'you_practice',
    5: 'you_add',
    6: 'autocheck'
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

    for number, file in enumerate(path.iterdir()):
        pass

    return number + 1


def enter_explanation_of_file():

    while True:
        try:
            user_input = input('Enter the short explanation of file: ').split()
            user_input = '_'.join(user_input)
            break
        except TypeError:
            print('Something wrong. Try again')

    return user_input


def main():

    # Отриммуємо шлях до папки де треба зробити шаблон
    my_path = get_parent_folder()

    # Отримуємо необхідну інформацію від користувача
    user_input_modul = enter_number_of_modul()
    user_input_type = choose_type()
    user_input_explanation = enter_explanation_of_file()

    # Отримуємо кількість файлів в папці, щоб присвоїти номер наступного файлу
    next_number_file = get_number_next_file_in_folder(my_path)

    file_name = '_'.join((user_input_modul, 
                      TYPES[user_input_type], 
                      str(next_number_file), 
                      user_input_explanation))
    
    path_of_new_file = os.path.abspath(f'{my_path}\{file_name}{TYPE_FILE}')
    print(file_name)

    with open(path_of_new_file, 'w') as file:
        print(f'File: {file_name} created. Path: {path_of_new_file}')


if __name__ == '__main__':

    main()