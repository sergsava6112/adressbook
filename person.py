#Класс для людей
class Person():
    def __init__(self):
        self.name = str(input('Введите Имя: '))
        self.surname = str(input('Введите Фамилию: '))
        self.email = str(input('Введите адрес электронной почты: '))
        self.number = str(input('Введите номер мобильного телефона: '))
        self.job = str(input('Введите название организации в которой работаете: '))

    def __str__(self):
        return f'{self.name}, {self.surname}, {self.email}, {self.number}, {self.job}'
