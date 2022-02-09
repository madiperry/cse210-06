""" Test by Jermain Lopez """
from keyboard_service import KeyboardService
import pytest
import pyray


class Test1:
    """
    class Test1:
    This class checks that inputs and outputs are received and sent from the service.
    """
    Keys = ['w', 'a', 's', 'd', 'i', 'j', 'k', 'l']
    arguments = [pyray.KEY_W, pyray.KEY_A, pyray.KEY_S, pyray.KEY_D, pyray.KEY_I, pyray.KEY_J, pyray.KEY_K, pyray.KEY_L]

    def test_is_key_up(self):
        """
        test_is_key_up():
        This function is responsible for verifying 
        the function when the key is not pressed, sending the letters of the key for verification.
        """

        for i in range(len(self.Keys)):
            object1 = KeyboardService()
            key_funtion = object1.is_key_up(self.Keys[i])
            Key_test = pyray.is_key_up(self.arguments[i])
            assert key_funtion == Key_test


    def test_is_key_down(self):
        """
        test_is_key_down():
        This function is responsible for verifying 
        the function when the key is pressed, sending the letters of the key for verification.
        """ 
 
        for i in range(len(self.Keys)):
            object1 = KeyboardService()
            key_funtion = object1.is_key_down(self.Keys[i])
            Key_test = pyray.is_key_down(self.arguments[i])
            assert key_funtion == Key_test

    def print_test1(self):
        print(self.test_is_key_up.__doc__) 
        print(self.test_is_key_down.__doc__)




 
test = Test1()
test.print_test1()
pytest.main(["-v", "--tb=line", "-rN", __file__])
