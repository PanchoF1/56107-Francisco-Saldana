import unittest
from clases import Calculator
class TestCalculador(unittest.TestCase):

    def resul_calculator_1_add_1_(self):

        calc = Calculator()

        calc.ingresar('1')

        calc.ingresar('+')

        calc.ingresar('1')

        calc.ingresar('=')

        self.assertEqual(calc.display(),'2')

    def resul_calculator_2_rest_1_(self):

        calc = Calculator()

        calc.ingresar('2')

        calc.ingresar('-')

        calc.ingresar('1')

        calc.ingresar('=')

        self.assertEqual(calc.display(),'1')

    def resul_calculator_2_x_2_(self):

        calc = Calculator()

        calc.ingresar('2')

        calc.ingresar('*')

        calc.ingresar('2')

        calc.ingresar('=')

        self.assertEqual(calc.display(),'4')

    def resul_calculator_10_div_5_(self):

        calc = Calculator()

        calc.ingresar('10')

        calc.ingresar('/')

        calc.ingresar('5')

        calc.ingresar('=')

        self.assertEqual(calc.display(),'2')

if __name__ == "__main__":

    unittest.main()