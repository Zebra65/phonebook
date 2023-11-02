#---------------------------------------
def show_menu():
    print("Телефонный справочник:")
    print(  "1. Распечатать справочник",
            "2. Найти телефон по фамилии",
            "3. Изменить номер телефона",
            "4. Удалит запись",
            "5. Найти абонента по номеру телефону",
            "6. Добавить абонента в справочник",
            "7. Закончить работу ", sep="\n",)
    choice = int(input("Введите номер строки меню: " ))
    #print  ("Меню: ", choice)
    return choice


def read_txt (filename):
    phone_book = []
    filds = ["Фамилия", "Имя", "Телефон", "Примечания"]

    with open(filename,'r',encoding='utf-8') as f:
        for line in f:
            record=dict(zip(filds,line.split(',')))
            phone_book.append(record)
    f.close()
    return phone_book

def write_txt(filename, phone_book):
    with open(filename,'w',encoding='utf-8') as f:
        for i in range(len(phone_book)):
            f.write(phone_book[i].get('Фамилия')+','+phone_book[i].get('Имя')+','+phone_book[i].get('Телефон')+','+phone_book[i].get('Примечания'))
    f.close()

def find_by_lastname(phone_book, last_name):
    key = []
    for i in range(len(phone_book)):
        if phone_book[i].get('Фамилия')==last_name:
            key.append(phone_book[i])
    return (key)

def find_by_number (phone_book, number):
    key = []
    for i in range(len(phone_book)):
        if phone_book[i].get('Телефон')==number:
            key.append(phone_book[i])
    return (key)

def change_number(phone_book, last_name, new_number):
    for i in range(len(phone_book)):
        if phone_book[i].get('Фамилия')==last_name:
            phone_book[i]['Телефон']=new_number
    write_txt('phonebook1.txt',phone_book)
    return phone_book

def delete_by_lastname(phone_book, last_name):
    a =0
    for i in range(0,len(phone_book)):
        if phone_book[i].get('Фамилия')==last_name:
            a = i
    phone_book.pop(a)
    write_txt('phonebook1.txt',phone_book)
    return phone_book

def add_user(phone_book, user_data):
    filds = ["Фамилия", "Имя", "Телефон", "Примечания"]
    record=dict(zip(filds,user_data.split(',')))
    record['Примечания']+='\n'
    phone_book.append(record)
    write_txt('phonebook1.txt',phone_book)
    return phone_book

def print_line(line):
    print(line.get('Фамилия')+' '+line.get('Имя')+' '+line.get('Телефон')+' '+line.get('Примечания'))

#------------------------------------------  


#def work_with_phonebook ():
choice = show_menu()
print ("Вы выбрали  меню: ", choice)

#-------------------------------------------------------
phone_book = read_txt('phonebook1.txt')
    #print(phone_book.read()) 
    # phone_book.close()
while (choice!=7):
    if choice==1:
        print("-----------------------")
        print("Телефонный справочник:")  
        for i in range(len(phone_book)):
            print_line(phone_book[i])
        print("-----------------------")
    elif choice==2:
        last_name= input('Поиск по Фамилии ')
        rez=find_by_lastname(phone_book, last_name)
        for i in range(len(rez)):
            print_line(rez[i])
    elif choice==3:
        last_name= input('Введите фамилию: ')
        new_number = input("Введите новый номер:")
        phone_book=change_number(phone_book, last_name, new_number)
        for i in range(len(phone_book)):
            print_line(phone_book[i])
    elif choice==4:
        last_name=input('Удаление контакта по фамилии: ')
        phone_book=delete_by_lastname(phone_book, last_name)
        for i in range(len(phone_book)):
            print_line(phone_book[i])
    elif choice==5:
        number=input('Введите номер для поиска: ')
        rez=find_by_number (phone_book, number)
        for i in range(len(rez)):
            print_line(rez[i])
    elif choice==6:
        user_data=input("Новый контакт: ")
        phone_book=add_user(phone_book, user_data)
        for i in range(len(phone_book)):
            print_line(phone_book[i])
    choice = show_menu()
    print ("Вы выбрали  меню: ", choice)
       
#work_with_phonebook ()

