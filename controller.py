from functions import  add_contact, find_contact, show_contacts, delete_contact
import my_menu



def run():
    my_menu.greetings()
    while True:
        choice = my_menu.menu()
        if choice == "1":
            surname = input('Введите фамилию:')
            name = input('Введите имя:')
            phone = input('Введите телефон:')
            surname = add_contact(surname, name, phone)
            my_menu.print_success(surname)
        elif choice == "2":
            surname = input("Введите фамилию контакта для поиска: ")
            contacts = find_contact(surname)
            my_menu.print_contacts(contacts)
        elif choice == "3":
            my_menu.print_contacts(show_contacts())
        elif choice == "4":
            surname = input('Введите фамилию:')
            name = input('Введите имя:')
            found = delete_contact(surname, name) 
            my_menu.print_delete(found, surname)            
        elif choice == "5":
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")
