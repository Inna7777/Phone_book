def greetings():
    print('**ТЕЛЕФОННАЯ КНИГА**')

def menu(): # меню программы
    print('\n Ваше желание:\n',
         '1-Добавить контакт \n',
         '2-Найти контакт \n',
         '3-Вывести все контакты \n',
         '4-Удалить контакт \n',
         '5-Закрыть книгу''\n')

    choice = input('Введите номер действия:')
    return choice


def print_success(surname): # результат добавления контакта
    print('Контакт {} добавлен.'.format(surname))


def print_contacts(contacts): #Вывод при вызове функции Find_contact
    if len(contacts) == 0:
        print('Контакт не найден')
    else:
        print('Найдены  контакты:')
        for contact in contacts:
            print(contact)


def print_delete(found, surname): # вывод результат удаления при вызове функции delet_contact
    if found == False:
        print('Контакт не найден')
    else:
        print('Контакт {} удален.'.format(surname))