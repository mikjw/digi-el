import pytest
from src import printer

@pytest.fixture(autouse=True)   
def test_printer():
    return printer.Printer()

class TestInitialization:
    def test_has_empty_inputs_dict(self, test_printer):
        assert test_printer.inputs == {}

    def test_has_input_count(self, test_printer):
        assert test_printer.input_count == 0

class TestInputCreation:
    def test_adds_input_a(self, test_printer):
        test_printer.add_input()
        assert test_printer.inputs['A'] == {'component': None, 'signal': None}

    def test_increments_input_counter_to_1(self, test_printer):
        test_printer.add_input()
        assert test_printer.input_count == 1

    def test_does_not_add_more_than_one_input(self, test_printer):
        with pytest.raises(KeyError):
            test_printer.add_input()
            test_printer.inputs['B']

    def test_adds_input_b(self, test_printer):
        for i in range(2):
            test_printer.add_input()
        assert test_printer.inputs['B'] == {'component': None, 'signal': None}

    def test_increments_input_counter_to_2(self, test_printer):
        for i in range(2):
            test_printer.add_input()
        assert test_printer.input_count == 2

    def test_does_not_add_more_than_two_inputs(self, test_printer):
        with pytest.raises(KeyError):
            for i in range(2):
                test_printer.add_input()
            test_printer.inputs['C']

    def test_adds_input_c(self, test_printer):
        for i in range(3):
            test_printer.add_input()
        assert test_printer.inputs['C'] == {'component': None, 'signal': None}

    def test_increments_input_counter_to_3(self, test_printer):
        for i in range(3):
            test_printer.add_input()
        assert test_printer.input_count == 3

    def test_does_not_add_more_than_three_inputs(self, test_printer):
        with pytest.raises(KeyError):
            for i in range(3):
                test_printer.add_input()
            test_printer.inputs['D']


