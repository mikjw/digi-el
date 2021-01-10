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
    def test_connects_line_to_src_comp_at_a(self, test_printer_2_inputs):
        assert isinstance(test_printer_2_inputs.inputs['A']['component'], line.Line)
    
    def test_connects_line_to_src_comp_at_b(self, test_printer_2_inputs):
        assert isinstance(test_printer_2_inputs.inputs['B']['component'], line.Line)

class TestSignalReceipt:    
    def test_receives_high_input_signal_at_a(self, test_printer, mocker):
        mock_line_in = mocker.Mock()
        test_printer.add_input()
        test_printer.connect_previous(mock_line_in, 'A')
        test_printer.receive_signal(mock_line_in, 'HIGH')
        assert test_printer.inputs['A']['signal'] == 'HIGH'

    def test_receives_low_input_signal_at_a(self, test_printer, mocker):
        mock_line_in = mocker.Mock()
        test_printer.add_input()
        test_printer.connect_previous(mock_line_in, 'A')
        test_printer.receive_signal(mock_line_in, 'LOW')
        assert test_printer.inputs['A']['signal'] == 'LOW'

    def test_receives_high_input_signal_at_b(self, test_printer, mocker):
        mock_line_in = mocker.Mock()
        test_printer.add_input(2)
        test_printer.connect_previous(mock_line_in, 'B')
        test_printer.receive_signal(mock_line_in, 'HIGH')
        assert test_printer.inputs['B']['signal'] == 'HIGH'
        
    def test_receives_low_input_signal_at_b(self, test_printer, mocker):
        mock_line_in = mocker.Mock()
        test_printer.add_input(2)
        test_printer.connect_previous(mock_line_in, 'B')
        test_printer.receive_signal(mock_line_in, 'LOW')
        assert test_printer.inputs['B']['signal'] == 'LOW'

class TestPrinting:
    def test_prints_output_high_low(self, capfd, mocker, test_printer):
        mock_line_in_a = mocker.Mock()
        mock_line_in_b = mocker.Mock()
        test_printer.add_input(2)
        test_printer.connect_previous(mock_line_in_a, 'A')
        test_printer.connect_previous(mock_line_in_b, 'B')
        test_printer.receive_signal(mock_line_in_a, 'HIGH')
        test_printer.receive_signal(mock_line_in_b, 'LOW')
        # test_printer.output_values()
        out, err = capfd.readouterr()
        assert out == 'A: HIGH | B: LOW\n'

    def test_prints_output_low_high(self, capfd, mocker, test_printer):
        mock_line_in_a = mocker.Mock()
        mock_line_in_b = mocker.Mock()
        test_printer.add_input(2)
        test_printer.connect_previous(mock_line_in_a, 'A')
        test_printer.connect_previous(mock_line_in_b, 'B')
        test_printer.receive_signal(mock_line_in_a, 'LOW')
        test_printer.receive_signal(mock_line_in_b, 'HIGH')
        # test_printer.output_values()
        out, err = capfd.readouterr()
        assert out == 'A: LOW | B: HIGH\n'
        
    def test_prints_when_all_inputs_have_signals(self, capfd, mocker, test_printer):
        mock_line_in_a = mocker.Mock()
        mock_line_in_b = mocker.Mock()
        test_printer.add_input(2)
        test_printer.connect_previous(mock_line_in_a, 'A')
        test_printer.connect_previous(mock_line_in_b, 'B')
        test_printer.receive_signal(mock_line_in_a, 'LOW')
        test_printer.receive_signal(mock_line_in_b, 'HIGH')
        out, err = capfd.readouterr()
        assert out == 'A: LOW | B: HIGH\n'
        
    def test_does_not_print_without_all_signals(self, capfd, mocker, test_printer):
        mock_line_in_a = mocker.Mock()
        mock_line_in_b = mocker.Mock()
        test_printer.add_input(2)
        test_printer.connect_previous(mock_line_in_a, 'A')
        test_printer.connect_previous(mock_line_in_b, 'B')
        test_printer.receive_signal(mock_line_in_a, 'LOW')
        out, err = capfd.readouterr()
        assert out == ''
