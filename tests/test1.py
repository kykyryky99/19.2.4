import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success_1(self):
        assert self.calc.multiply(self, 3, 2) == 6

    def test_adding_success_2(self):
        assert self.calc.division(self, 6, 2) == 3

    def test_adding_success_3(self):
        assert self.calc.subtraction(self, 10, 5) == 5

    def test_adding_success_4(self):
        assert self.calc.adding(self, 15, 2) == 17

    def test_division_zero(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def teardown(self):
        print('Выполнение Teardown')