import pytest
from src import container

@pytest.fixture(autouse=True)   
def test_container():
    return container.Container()

class TestInitialization:
    def test_input(self, test_container):
        assert test_container.inputs['A'] == {'inner_component': None, 'outer_component': None, 'signal': None}
        
    def test_output(self, test_container):
        assert test_container.outputs['Z'] == {'inner_component': None, 'outer_component': None, 'signal': None}
        
    def test_inits_with_input_count(self, test_container):
        assert test_container.input_count == 1
        
    def test_inits_with_output_count(self, test_container):
        assert test_container.output_count == 1
        
    def test_increments_5_inputs_on_initialization(self):
        test_container_2 = container.Container(5)
        assert test_container_2.input_count == 5
        
    def test_creates_5_inputs_on_initialization(self):
        test_container_2 = container.Container(5)
        assert 'E' in test_container_2.inputs
        
    def test_increments_12_inputs_on_initialization(self):
        test_container_2 = container.Container(12)
        assert test_container_2.input_count == 12
        
    def test_creates_12_inputs_on_initialization(self):
        test_container_2 = container.Container(12)
        assert 'L' in test_container_2.inputs
    
class TestGetter:
    def test_get_outputs_returns_outputs(self, test_container):
        assert test_container.get_outputs() == {'Z': {'inner_component': None, 'outer_component': None, 'signal': None}}
        
class TestInputCreation:
    def test_adds_input_b(self, test_container):
        test_container.add_input()
        assert test_container.inputs['B'] == {'inner_component': None, 'outer_component': None, 'signal': None}
        
    def test_adds_input_c(self, test_container):
        test_container.add_input(2)
        assert test_container.inputs['C'] == {'inner_component': None, 'outer_component': None, 'signal': None}
     
    def test_adds_input_e(self, test_container):
        test_container.add_input(9)
        assert test_container.inputs['J'] == {'inner_component': None, 'outer_component': None, 'signal': None}
        
    def test_increments_input_count_to_2(self, test_container):
        test_container.add_input()
        assert test_container.input_count == 2
        
    def test_increments_input_count_to_3(self, test_container):
        test_container.add_input(2)
        assert test_container.input_count == 3
        
    def test_increments_input_count_to_9(self, test_container):
        test_container.add_input(8)
        assert test_container.input_count == 9
        
    def test_limits_input_count_to_13(self, test_container):
        test_container.add_input(12)
        test_container.add_input()
        assert test_container.input_count == 13
        
    def test_prints_input_count_limit_error(self, capfd, test_container):
        test_container.add_input(16)
        out, err = capfd.readouterr()
        assert out == "Cannot add input - limit reached\n"

class TestOutputCreation:
    def test_starts_with_output_z(self, test_container):
        assert test_container.outputs['Z'] == {'inner_component': None, 'outer_component': None, 'signal': None}

    def test_adds_output_y(self, test_container):
        test_container.add_output()
        assert test_container.outputs['Y'] == {'inner_component': None, 'outer_component': None, 'signal': None}
        
    def test_adds_output_x(self, test_container):
        test_container.add_output(2)
        assert test_container.outputs['X'] == {'inner_component': None, 'outer_component': None, 'signal': None}
     
    def test_adds_output_q(self, test_container):
        test_container.add_output(9)
        assert test_container.outputs['Q'] == {'inner_component': None, 'outer_component': None, 'signal': None}
        
    def test_increments_output_count_to_2(self, test_container):
        test_container.add_output()
        assert test_container.output_count == 2
        
    def test_increments_output_count_to_3(self, test_container):
        test_container.add_output(2)
        assert test_container.output_count == 3
        
    def test_increments_output_count_to_9(self, test_container):
        test_container.add_output(8)
        assert test_container.output_count == 9
        
    def test_limits_output_count_to_13(self, test_container):
        test_container.add_output(12)
        test_container.add_output()
        assert test_container.output_count == 13
        
    def test_prints_output_count_limit_error(self, capfd, test_container):
        test_container.add_output(16)
        out, err = capfd.readouterr()
        assert out == "Cannot add output - limit reached\n"

class TestConnectWithin:
    def test_connects_to_component_at_input_a(self, test_container, mocker):
        test_line = mocker.Mock()
        test_container.connect_within(test_line, 'A')
        assert test_container.inputs['A']['inner_component'] == test_line      
    
    def test_connects_to_component_at_input_b(self, test_container, mocker):
        test_line = mocker.Mock()
        test_container.add_input()
        test_container.connect_within(test_line, 'B')
        assert test_container.inputs['B']['inner_component'] == test_line
     
    def test_calls_connect_previous_on_comp(self, test_container, mocker):
        mock_line = mocker.Mock()
        test_container.connect_within(mock_line, 'A')
        mock_line.connect_previous.assert_called_with(test_container)
        
class TestConnectPrevious:
    def test_connects_previous_at_z(self, test_container, mocker):
        mock_line = mocker.Mock()
        test_container.connect_previous(mock_line, 'Z')
        assert test_container.outputs['Z']['inner_component'] == mock_line
        
    def test_connects_previous_at_y(self, test_container, mocker):
        mock_line = mocker.Mock()
        test_container.add_output()
        test_container.connect_previous(mock_line, 'Y')
        assert test_container.outputs['Y']['inner_component'] == mock_line

    def test_notifies_when_invalid_output_terminal_y(self, capfd, test_container, mocker):
        mock_line = mocker.Mock()
        test_container.connect_previous(mock_line, 'Y')
        out, err = capfd.readouterr()
        assert out == "Connection failed - invalid terminal on container\n"

    def test_does_not_notify_valid_output_terminal_y(self, capfd, test_container, mocker):
        mock_line = mocker.Mock()
        test_container.add_output()
        test_container.connect_previous(mock_line, 'Y')
        out, err = capfd.readouterr()
        assert out == ''

    def test_assigns_output_outer_comp_for_n(self, test_container, mocker):
        mock_line = mocker.Mock()
        test_container.add_output(12)
        test_container.connect_previous(mock_line, 'N')
        assert test_container.outputs['N']['inner_component'] == mock_line

    def test_assigns_input_inner_comp_for_m(self, test_container, mocker):
        mock_line = mocker.Mock()
        test_container.add_input(12)
        test_container.connect_previous(mock_line, 'M')
        assert test_container.inputs['M']['outer_component'] == mock_line

    def test_assigns_input_inner_comp_for_a(self, test_container, mocker):
        mock_line = mocker.Mock()
        test_container.connect_previous(mock_line, 'A')
        assert test_container.inputs['A']['outer_component'] == mock_line

    def test_assigns_input_inner_comp_for_b(self, test_container, mocker):
        mock_line = mocker.Mock()
        test_container.add_input()
        test_container.connect_previous(mock_line, 'B')
        assert test_container.inputs['B']['outer_component'] == mock_line

    def test_assigns_input_inner_comp_for_c(self, test_container, mocker):
        mock_line = mocker.Mock()
        test_container.add_input(2)
        test_container.connect_previous(mock_line, 'C')
        assert test_container.inputs['C']['outer_component'] == mock_line

    def test_notifies_invalid_input_terminal_b(self, capfd, test_container, mocker):
        mock_line = mocker.Mock()
        test_container.connect_within(mock_line, 'B')
        out, err = capfd.readouterr()
        assert out == "Connection failed - invalid input terminal on container\n"
        
    def test_notifies_invalid_input_terminal_c(self, capfd, test_container, mocker):
        mock_line = mocker.Mock()
        test_container.connect_within(mock_line, 'C')
        out, err = capfd.readouterr()
        assert out == "Connection failed - invalid input terminal on container\n"
        
    def test_does_not_notify_valid_input_terminal_b(self, capfd, test_container, mocker):
        mock_line = mocker.Mock()
        test_container.add_input()
        test_container.connect_within(mock_line, 'B')
        out, err = capfd.readouterr()
        assert out == ''

class TestConnectNext:
    def test_connects_to_next_at_z(self, test_container, mocker):
        mock_line = mocker.Mock()
        test_container.connect_next(mock_line, 'Z')
        assert test_container.outputs['Z']['outer_component'] == mock_line

    def test_connects_to_next_at_y(self, test_container, mocker):
        mock_line = mocker.Mock()
        test_container.add_output()
        test_container.connect_next(mock_line, 'Y')
        assert test_container.outputs['Y']['outer_component'] == mock_line

    def test_notifies_when_terminal_y_is_invalid(self, capfd, test_container, mocker):
        mock_line = mocker.Mock()
        test_container.connect_next(mock_line, 'Y')
        out, err = capfd.readouterr()
        assert out == "Connection failed - invalid terminal on container\n"

    def test_does_not_notify_when_terminal_y_is_valid(self, capfd, test_container, mocker):
        mock_line = mocker.Mock()
        test_container.add_output()
        test_container.connect_next(mock_line, 'Y')
        out, err = capfd.readouterr()
        assert out == ''

    def test_calls_connect_previous_on_outer_comp(self, test_container, mocker):
        mock_line = mocker.Mock()
        test_container.connect_next(mock_line, 'Z')
        mock_line.connect_previous.assert_called_with(test_container)

class TestSignalReceipt:    
    def test_receives_high_input_signal_at_a(self, test_container, mocker):
        mock_line_in = mocker.Mock()
        mock_line_out = mocker.Mock()
        test_container.connect_previous(mock_line_in, 'A')
        test_container.connect_within(mock_line_out, 'A')
        test_container.receive_signal(mock_line_in, 'HIGH')
        assert test_container.inputs['A']['signal'] == 'HIGH'

    def test_receives_low_input_signal_at_a(self, test_container, mocker):
        mock_line_in = mocker.Mock()
        mock_line_out = mocker.Mock()
        test_container.connect_previous(mock_line_in, 'A')
        test_container.connect_within(mock_line_out, 'A')
        test_container.receive_signal(mock_line_in, 'LOW')
        assert test_container.inputs['A']['signal'] == 'LOW'

    def test_receives_high_input_signal_at_b(self, test_container, mocker):
        mock_line_in = mocker.Mock()
        mock_line_out = mocker.Mock()
        test_container.add_input()
        test_container.connect_previous(mock_line_in, 'B')
        test_container.connect_within(mock_line_out, 'B')
        test_container.receive_signal(mock_line_in, 'HIGH')
        assert test_container.inputs['B']['signal'] == 'HIGH'

    def test_receives_high_input_signal_at_f(self, test_container, mocker):
        mock_line_in = mocker.Mock()
        mock_line_out = mocker.Mock()
        test_container.add_input(5)
        test_container.connect_previous(mock_line_in, 'F')
        test_container.connect_within(mock_line_out, 'F')
        test_container.receive_signal(mock_line_in, 'HIGH')
        assert test_container.inputs['F']['signal'] == 'HIGH'

    def test_receives_high_input_signal_at_z(self, test_container, mocker):
        mock_line_in = mocker.Mock()
        mock_line_out = mocker.Mock()
        test_container.connect_previous(mock_line_in, 'Z')
        test_container.connect_next(mock_line_out, 'Z')
        test_container.receive_signal(mock_line_in, 'HIGH')
        assert test_container.outputs['Z']['signal'] == 'HIGH'

    def test_receives_low_input_signal_at_z(self, test_container, mocker):
        mock_line_in = mocker.Mock()
        mock_line_out = mocker.Mock()
        test_container.connect_previous(mock_line_in, 'Z')
        test_container.connect_next(mock_line_out, 'Z')
        test_container.receive_signal(mock_line_in, 'LOW')
        assert test_container.outputs['Z']['signal'] == 'LOW'

    def test_receives_high_input_signal_at_y(self, test_container, mocker):
        mock_line_in = mocker.Mock()
        mock_line_out = mocker.Mock()
        test_container.add_output()
        test_container.connect_previous(mock_line_in, 'Y')
        test_container.connect_next(mock_line_out, 'Y')
        test_container.receive_signal(mock_line_in, 'HIGH')
        assert test_container.outputs['Y']['signal'] == 'HIGH'

class TestSignalTransmission:
    def test_transmits_to_inner_component_on_input(self, test_container, mocker):
        mock_line_in = mocker.Mock()
        mock_line_out = mocker.Mock()
        test_container.connect_previous(mock_line_in, 'A')
        test_container.connect_within(mock_line_out, 'A')
        test_container.receive_signal(mock_line_in, 'HIGH')
        mock_line_out.receive_signal.assert_called_with('HIGH')

    def test_transmits_to_inner_component_on_output(self, test_container, mocker):
        mock_line_in = mocker.Mock()
        mock_line_out = mocker.Mock()
        test_container.connect_previous(mock_line_in, 'Z')
        test_container.connect_next(mock_line_out, 'Z')
        test_container.receive_signal(mock_line_in, 'HIGH')
        mock_line_out.receive_signal.assert_called_with('HIGH')

