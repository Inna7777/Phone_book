def add_contact(surname, name, phone): # функция записи контакта в телефонную книгу
    with open ('phonenum.txt', 'a+', encoding='utf-8') as file: # открываем файл для записи
        file.write(surname + ' '+ name + ' :' + phone + '\n') # записываем данные в строчку и переходим на новую
    return surname