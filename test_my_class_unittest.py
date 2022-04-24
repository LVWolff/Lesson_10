

import unittest

from my_class import T_Class

class TestMyClass_unittest(unittest.TestCase):

    def setUp(self):
        print('Start test')
        self.my_class = T_Class('Мой тестовый класс')

    def tearDown(self):
        print('Test complited')
        del self.my_class

    def test_init(self):
        self.assertEqual(self.my_class.name_ob, 'Мой тестовый класс')

    def test_change_num1(self):
        num_1 = self.my_class.number_1
        self.my_class.change_number_1(60)
        self.assertTrue(self.my_class.number_1 == 60)


