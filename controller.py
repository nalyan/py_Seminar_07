import view
import model

def menu():
    val = view.menu_view()
    if val == 'user_input': write()
    elif val == 'user_convert': model.convert()
    else: exit

def write():
    data = view.data_input()
    model.write_csv(data)
    ask = view.ask()

    if ask == True: write()
    else: menu()
