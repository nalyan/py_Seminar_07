import os.path
import controller

def write_csv(data_inp):
    with open('phones.csv', 'a', encoding='utf_8') as data:
        data.write(data_inp)
def convert():
    check_file = os.path.exists('phones.csv')
    if check_file == True:
        with open('phones.csv', 'r', encoding='utf_8') as data:
            with open('phones.txt', 'w') as txt_file:
                text = data.read().split(',')
                txt_file.write('\n'.join(text))
                controller.menu()
    else:
        print('!!! The file has not been created yet !!!')
        controller.menu()
