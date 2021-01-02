import pytest
from src import line
from src import printer
from src import container

@pytest.fixture(autouse=True)  
def test_printer():
    return printer.Printer()

@pytest.fixture(autouse=True) 
def dummy_container():
    return container.Container()

@pytest.fixture(autouse=True)  
def printer_with_container(dummy_container):
    return printer.Printer(dummy_container)

@pytest.fixture(autouse=True) 
def dummy_container_2_outputs():
    return container.Container(2, 2)

@pytest.fixture(autouse=True)  
def test_printer_2_inputs(dummy_container_2_outputs):
    return printer.Printer(dummy_container_2_outputs)

class TestInitialization:
    def test_has_empty_inputs_dict(self, test_printer):
        assert test_printer.inputs == {}

    def test_has_input_count(self, test_printer):
        assert test_printer.input_count == 0
        
    def test_initializes_with_container(self, printer_with_container, dummy_container):
        assert printer_with_container.source_component == dummy_container

    def test_adds_inputs_matching_container_outputs(self, test_printer_2_inputs):
        assert test_printer_2_inputs.input_count == 2

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

class TestConnection:
    def test_connects_to_previous_component(self, test_printer_2_inputs, mocker):
        mock_component = mocker.Mock()
        test_printer_2_inputs.connect_previous(mock_component, 'A')
        assert test_printer_2_inputs.inputs['A']['component'] == mock_component
        
class TestSourceConnection:
    def test_connects_lines_to_src_comp(self, test_printer_2_inputs):
        assert isinstance(test_printer_2_inputs.inputs['B'], line.Line)




