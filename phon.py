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
#------------------------------------------        
def work_with_phonebook ():
    choice = show_menu()
    print ("Вы выбрали  меню: ", choice)

#-------------------------------------------------------
    phone_book = open('phonebook.txt', mode='rt') #открытие файла
    #print(phone_book.read()) 
    # phone_book.close()
    
    while (choice!=7):
            if choice==1:
                print("-----------------------")
                print("Телефонный справочник:")  
                print( phone_book.read())  
                print("-----------------------")
                phone_book.close() 
                #choice = show_menu()
                work_with_phonebook ()
            elif choice==2:
                last_name= input('Поиск по Фамилии ')
                #print(find_by_lastname, (phone_book, last_name))
                read_txt()
                print(find_by_lastname, (phone_book, last_name))
                phone_book.close() 
            elif choice==3:
                last_name= input('lastname ')
                new_number = input("new_number")
                print(change_number(phone_book, last_name, new_number))
            elif choice==4:
                lastname=input('lastname ')
                print (delete_by_lastname(phone_book, last_name))
            elif choice==5:
                number=input('number ')
                print (find_by_number (phone_book, number))
            elif choice==6:
                user_data=input("new data ")
                add_user (phone_book, user_data)
                write_txt('phonebook.txt, phone_book ')  
               
#--------------------------------------------   
#Lne_book = open('phonebook.txt', mode='rt') #открытие файла
    # phone_book = open('phonebook.txt', 'r') #открытие файла
    # print(phone_book.read()) 
    # phone_book.close()
def read_txt (phone_book):
    phone_book [filds]
    filds = ["Фамилия", "Имя", "Телефон", "Примечания"]

work_with_phonebook ()

