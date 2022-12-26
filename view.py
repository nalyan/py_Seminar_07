
def menu_view():
    print('--------------------')
    print('1. Ввод данных')
    print('2. Сохранить в .txt')
    print('3. Выход')
    print('--------------------')

    while True:
        choice = int(input('Выберите номер действия (1, 2, 3): '))
        if choice == 1:
            return 'user_input'
            break
        elif choice == 2:
            return 'user_convert'
            break
        elif choice == 3:
            return 'exit'
            break

def data_input():
    surname = input('Введите Фамилию: ')
    name = input('Введите Имя: ')
    patron = input('Введите отчество: ')
    phone_num = input('Введите номер телефона: ')
    return f'{surname},{name},{patron},{phone_num}\n'

def ask():
   while True:
        ask_input = input('Продолжить ввод (Y/N): ')
        if ask_input == 'Y' or ask_input == 'y':
            return True
            break
        elif ask_input == 'N' or ask_input == 'n':
            return False
            break
