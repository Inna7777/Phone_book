def add_contact(surname, name, phone): # функция записи контакта в телефонную книгу
    with open ('phonenum.txt', 'a+', encoding='utf-8') as file: # открываем файл для записи
        file.write(surname + ' '+ name + ' :' + phone + '\n') # записываем данные в строчку и переходим на новую
    return surname


def find_contact(surname): # поиск контакта
    contacts = [] # создаем пустой список
    with open('phonenum.txt', 'r', encoding='utf-8') as file: # открываем файл для чтения
        for line in file:
            if surname in line: 
                contacts.append(line.strip()) # если контакт найден записывем в список
    return contacts # возвращаем список контактов


def show_contacts(): # показываем список контактов
    contacts = []
    with open ('phonenum.txt', 'r', encoding = "utf-8") as file: # открываем файл для чтения
        for line in file: 
            contacts.append(line.strip()) # записываем контакты построчно
    return(contacts)


def delete_contact(surname, name): #  удаление контакта
    with open('phonenum.txt', 'r+', encoding='utf-8') as file: # открываем файл
        s = file.readlines() #читает все строки из файла и возвращает их в виде списка строк
        found = False # проверка на выполнения действия удаления
        for i in reversed(range( len(s))):
            if surname  in s[i] and name in s[i]: # если фамилия и имя совпали
                s.pop(i) # удаляем контакт
                found = True
        if found == False: # ecли контакт не найден
            return (found) # возвращаем "лож"
    with open('phonenum.txt', 'w', encoding='utf-8') as file_1: # открываем файл для записи
        file_1.writelines(i for i in s) # переписываем неудаленные контакты
    return (found) # возврвщвем "Правда"
