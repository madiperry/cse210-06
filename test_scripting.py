""" Test by Jermain Lopez """
from script import Script
import pyray
import pytest

class Test3:
    """
    class Test3:
    This class checks the inputs and outputs of move commands.
    """

    def test_add_input_action(self):
        """
        test_add_input_action():
        This method verifies that control actions are added correctly.
        """
        self.keys_list = ['w', 'a', 's', 'd', 'i', 'j', 'k', 'l']
        number_key = [87, 65, 83, 68, 73, 74, 75, 76]
        self.arguments_list = [pyray.KEY_W, pyray.KEY_A, pyray.KEY_S, pyray.KEY_D, pyray.KEY_I, pyray.KEY_J, pyray.KEY_K, pyray.KEY_L]
    
        for key in range(len(self.keys_list)):

            script = Script()
            script.add_action(self.keys_list[key], self.arguments_list[key])
            each_imput = script.get_actions(self.keys_list[key])
            assert each_imput[0] == number_key[key]

    def test_add_output_action(self):
        """
        test_add_output_action():
        This method verifies that control actions are returned correctly.
        """
        self.keys_list = ['w', 'a', 's', 'd', 'i', 'j', 'k', 'l']
        number_key = [87, 65, 83, 68, 73, 74, 75, 76]
        self.arguments_list = [pyray.KEY_W, pyray.KEY_A, pyray.KEY_S, pyray.KEY_D, pyray.KEY_I, pyray.KEY_J, pyray.KEY_K, pyray.KEY_L]
        for key in range(len(self.keys_list)):

            script = Script()
            script.add_action(self.keys_list[key], self.arguments_list[key])
            each_output = script.get_actions(self.keys_list[key])
            assert each_output[0]  == number_key[key]


    def print_tests(self):
        print(self.test_add_input_action.__doc__) 
        print(self.test_add_output_action.__doc__)



test3 = Test3()
test3.print_tests()
pytest.main(["-v", "--tb=line", "-rN", __file__])
