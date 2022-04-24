
import pytest

from my_class import T_Class

class TestClass_pytest:

    def setup(self):
        self.myClass = T_Class('Тестовый класс')
        print('Start test')

    def teardown(self):
        del self.myClass
        print('Test complited')

    def test_init(self):
        assert self.myClass.name_ob == 'Тестовый класс'

    def test_change_num1(self):
        self.myClass.change_number_1(50)
        assert self.myClass.number_1 == 50

    def test_change_name_ob(self):
        self.myClass.change_name_ob('Новое наименование объекта')
        assert self.myClass.name_ob == 'Новое наименование объекта'

