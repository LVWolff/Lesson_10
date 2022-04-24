# конечно можно использовать декорацию @propety

import random
class T_Class:

    def __init__(self, name):
        self.name_ob = name
        self.number_1 = random.randint(1, 100)
        self.number_2 = random.randint(1, 100)

        self.__hidden_propetice = name + ' (hidden)'

    def __str__(self):
        return 'Тестовый класс: ' + self.name_ob

    def __hiddem_method(self):
        print("Код выполняемый в скрытой функции класса")
        print("Скрытое свойство:", self.__hidden_propetice)

    def t_func(self):
        self.__hiddem_method()
        print('Код выполяемый в тестовом методе класса')

    def change_number_1(self, num):
        if self.number_1 == num:
            pass
        elif 1 <= num <= 100:
            self.number_1 = num
        else:
            pass

    def change_number_2(self, num):
        if self.number_2 == num:
            pass
        elif 1 <= num <= 100:
            self.number_2 = num
        else:
            pass

    def change_name_ob(self, new_name):
        if self.name_ob != new_name:
            self.name_ob = new_name
        else:
            print('Наименование не изменилось')


if __name__ == '__main__':
    t_class = T_Class('test class 1')
    print(t_class)
    t_class.t_func()
