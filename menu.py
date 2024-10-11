import valid as v

def print_welcome():
    # This is the welcome message
    print('\nWelcome Message')

def print_menu():
    # These are the menu options
    print('\nMENU')
    print('\n1. Option 1'
         +'\n2. Option 2'
         +'\n3. Option 3'
         +'\n4. Option 4')

def get_menu_choice():
    # This is the user input for the menu opitions
    menu_choice = 0
    menu_choice = v.get_integer('\nChoose Menu Option: ')
    while menu_choice < 0 or menu_choice > 4:
        print('Invalid input.')
        print_menu()
        menu_choice = int(input('\nChoose Menu Option: '))
    return menu_choice 
