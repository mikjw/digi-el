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

    def test_adds_input_b(self, test_printer):
        for i in range(2):
            test_printer.add_input()
        assert test_printer.inputs['B'] == {'component': None, 'signal': None}

    def test_increments_input_counter_to_2(self, test_printer):
        for i in range(2):
            test_printer.add_input()
        assert test_printer.input_count == 2

