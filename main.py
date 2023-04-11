def print_item(d, i):
    print(f"ID: {d[i][0]},\t Фамилия: {d[i][1]},\t Имя: {d[i][2]},\t"
          + f"Отчество: {d[i][3]},\t Телефон: {d[i][4]}")

def read_file(filename):
    with open(filename, 'r') as data:
        data_array = []
        for line in data:
            item = line.replace('\n','').replace(' ','').split(sep = ',')
            data_array.append(item)
    return data_array

def write_file(filename, data_array):
    with open(filename, 'w') as data:
        for i in data_array:
            write_element = ','.join(i)
            data.write(f'{write_element}\n')

def add_item(filename, lastname = '', firstname = '', secondname = '', phone = ''):
    data_array = read_file(filename) 
    max_id = 0
    for i in range(1,len(data_array)):
        if max_id < int(data_array[i][0]): 
            max_id = int(data_array[i][0])
    next_id = max_id + 1
    # print(next_id)
    lastname = input('Фамилия: ')
    firstname = input('Имя: ')
    secondname = input('Отчество: ')
    phone = input('Телефон: ')
    new_item = []
    new_item.append(str(next_id))
    new_item.append(lastname)
    new_item.append(firstname)
    new_item.append(secondname)
    new_item.append(phone)
    # print(new_item)
    # print(data_array)
    data_array.append(new_item)
    # print(data_array)
    for i in range(1,len(data_array)):
        print_item(data_array, i)
    write_file(filename, data_array)

def show_all_items(filename):
    data_array = read_file(filename)    
    for i in range(1,len(data_array)):
        print_item(data_array, i)

def change_items(filename):
    data_array = read_file(filename) 
    for i in range(1,len(data_array)):
        print_item(data_array, i)
    print(' ')
    id_delete = int(input('Введите номер id записи для редактирования: '))
    index_id = -1
    for i in range(1,len(data_array)):
        if id_delete == int(data_array[i][0]):
            index_id = i
            break
    if index_id != -1:
        print_item(data_array, i)
        print(' ')
        print('Введите номер редактируемого параметра!')
        user_operation = 0 
        while(user_operation != 5):
            print('1 - Редактировать Фамилию')
            print('2 - Редактировать Имя')
            print('3 - Редактировать Отчество')
            print('4 - Редактировать Телефон')
            print('5 - Сохранить')
            user_operation = int(input('Введите номер операции: '))
            if user_operation == 1:
                lastname = input('Фамилия: ')
                data_array[index_id][1] = lastname
            elif user_operation == 2:
                firstname = input('Имя: ')
                data_array[index_id][2] = firstname
            elif user_operation == 3:
                secondname = input('Отчество: ')
                data_array[index_id][3] = secondname
            elif user_operation == 4:
                phone = input('Телефон: ')
                data_array[index_id][4] = phone
            elif user_operation > 5:
                print('Ошибка ввода!!!')
            print(' ')
            
        print_item(data_array, i)
        write_file(filename, data_array)
    else:
        print("ID не найден!!!")

def delete_items(filename):
    data_array = read_file(filename)
    for i in range(1,len(data_array)):
        print_item(data_array, i)   
    id_delete = int(input('Введите номер id удаляемой записи: '))
    for i in range(1,len(data_array)):
        if id_delete == int(data_array[i][0]):
            del data_array[i]
            break
    print(' ')
    for i in range(1,len(data_array)):
        print_item(data_array, i)
    write_file(filename, data_array)


def menu():
    print('Добро пожаловать в телефонный справочник!')
    print('1 - Показать все записи')
    print('2 - Добавить запись')
    print('3 - Изменить запись')
    print('4 - Удалить запись')
    user_operation = int(input('Введите номер операции: '))
    print(' ')

    if user_operation == 1:
        show_all_items(filename)
    elif user_operation == 2: 
        add_item(filename)
    elif user_operation == 3:
        change_items(filename)
    elif user_operation == 4:
        delete_items(filename)

filename = 'file.txt'
menu()