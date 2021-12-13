from person import Person



def main():
    while True:
        print('Выбери действие: 1-добавление/2 - показать все/3-удаление всего и вся: ')
        option = int(input('Действие: '))
        if option == 1:
            with open('adress_book_1.txt', 'a') as file:
                file.write(str(Person()))
                file.write(str('\n'))
        elif option == 2:
            with open('adress_book_1.txt', 'r') as file:
                print(file.read())

        elif option == 3:
                with open('adress_book_1.txt', 'w') as file:
                    file.write(str('\n'))
                print('Все записи удалены!')
                break

main()