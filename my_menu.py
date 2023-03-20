def greetings():
    print('**ТЕЛЕФОННАЯ КНИГА**')

def menu():
    print('Ваше желание:\n',
         '1-Добавить контакт \n',
         '2-Найти контакт \n',
         '3-Вывести все контакты \n',
         '4-Удалить контакт \n',
         '5-Закрыть книгу''\n')

    choice = input('Введите номер действия:')
    return choice


def print_success(surname):
    print('Контакт {} добавлен.'.format(surname))


def print_contacts(contacts):
    if len(contacts) == 0:
        print('Контакт не найден')
    else:
        print('Найдены  контакты:')
        for contact in contacts:
            print(contact)


def print_delete(found, surname):
    if found == False:
        print('Контакт не найден')
    else:
        print('Контакт {} удален.'.format(surname))