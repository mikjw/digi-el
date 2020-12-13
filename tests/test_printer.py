import pytest
from src import printer
from src import container

@pytest.fixture(autouse=True) 
def dummy_container():
    return container.Container()
 
@pytest.fixture(autouse=True)  
def test_printer(dummy_container):
    return printer.Printer(dummy_container)

class TestInitialization:
    def test_has_empty_inputs_dict(self, test_printer):
        assert test_printer.inputs == {}

    def test_has_input_count(self, test_printer):
        assert test_printer.input_count == 0
        
    def test_initializes_with_container(self, test_printer, dummy_container):
        assert test_printer.source_component == dummy_container

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

    def test_adds_2_inputs_when_passed_2(self, test_printer):
        test_printer.add_input(2)
        assert test_printer.input_count == 2

    def test_adds_input_b_when_passed_2(self, test_printer):
        test_printer.add_input(2)
        assert test_printer.inputs['B'] == {'component': None, 'signal': None}

    def test_adds_5_inputs_when_passed_5(self, test_printer):
        test_printer.add_input(5)
        assert test_printer.input_count == 5

    def test_adds_input_e_when_passed_5(self, test_printer):
        test_printer.add_input(5)
        assert test_printer.inputs['E'] == {'component': None, 'signal': None}

    def test_adds_default_1_input_passed_nothing(self, test_printer):
        test_printer.add_input()
        assert test_printer.input_count == 1




