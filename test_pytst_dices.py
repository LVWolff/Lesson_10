
import pytest

from encapsulation import Dice_inc

class TestDice_pytest:

    def setup(self):
        self.dice_game = Dice_inc(3)
        print('Start test')

    def teardown(self):
        self.dice_game.current_throw = 0
        print('Test has done')

    def test_init(self):
        assert self.dice_game.throw_num == 3
        assert self.dice_game.current_throw == 0

    def test_dice_setter(self):
        self.dice_game.hidden_num_1 = 5
        self.dice_game.hidden_num_2 = 5
        assert (self.dice_game.hidden_num_1 == 5) & (self.dice_game.hidden_num_2 == 5)

        with pytest.raises(ValueError): #
            #Код вызывающий данную ошибку
            self.dice_game.hidden_num_1 = 8

    def test_throw_dices(self):
        # self.dice_game.hidden_num_1 = 5
        # self.dice_game.hidden_num_2 = 5
        self.dice_game.set_hidden_numbers()
        self.dice_game.throw_dices()
        assert self.dice_game.current_throw == 1
        self.dice_game.throw_dices()
        assert self.dice_game.current_throw == 2

    def test_change_dices(self):
        self.dice_game.set_hidden_numbers()
        dice1 = self.dice_game.hidden_num_1
        dice2 = self.dice_game.hidden_num_2

        self.dice_game.change_dices()

        assert {dice1, dice2} != {self.dice_game.hidden_num_1, self.dice_game.hidden_num_2}





