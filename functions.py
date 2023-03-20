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


def delete_contact(surname, name):
    with open('phonenum.txt', 'r+', encoding='utf-8') as file:
        s = file.readlines()
        found = False
        for i in reversed(range( len(s))):
            if s['name'] == name and s['surname'] == surname in s[i]:
                s.pop(i)
                s.pop(i-1)
                s.pop(i-2)
                found = True
                break
            if found == False:
                return f'{name} {surname} not found'
    with open('phonenum.txt', 'w', encoding='utf-8') as file_1:
        file_1.writelines(i for i in s)
    return (surname)
