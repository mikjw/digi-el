import pytest
from src import nand

@pytest.fixture(autouse=True)   
def test_nand():
    return nand.Nand()

class TestInitialization:
    def test_input_connection_a(self, test_nand):
        assert test_nand.in_connection_a == None
        
    def test_input_connection_b(self, test_nand):
        assert test_nand.in_connection_b == None
        
    def test_input_signal_a(self, test_nand):
        assert test_nand.in_signal_a == None
        
    def test_input_signal_b(self, test_nand):
        assert test_nand.in_signal_b == None
        
    def test_output_connection(self, test_nand):
        assert test_nand.out_connection == None
        
    def test_output_signal(self, test_nand):
        assert test_nand.out_signal == None
        
class TestConnection:
    def test_connects_to_next_component(self, test_nand, mocker):
        mock_line = mocker.Mock()
        test_nand.connect_next(mock_line)
        assert test_nand.out_connection == mock_line
        
    def test_connects_to_previous_comp_on_a(self, test_nand, mocker):
        mock_line = mocker.Mock()
        test_nand.connect_previous(mock_line, 'A')
        assert test_nand.in_connection_a == mock_line
        
    def test_connects_to_previous_comp_on_b(self, test_nand, mocker):
        mock_line = mocker.Mock()
        test_nand.connect_previous(mock_line, 'B')
        assert test_nand.in_connection_b == mock_line
                
    def test_calls_connect_previous_on_next_comp(self, test_nand, mocker):
        mock_line = mocker.Mock()
        test_nand.connect_next(mock_line)
        mock_line.connect_previous.assert_called_with(test_nand)
        
    def test_notifies_invalid_input_terminal_C(self, capfd, test_nand, mocker):
        mock_line = mocker.Mock()
        test_nand.connect_previous(mock_line, 'C')
        out, err = capfd.readouterr()
        assert out == "Connection failed - invalid input terminal\n"
        
    def test_notifies_invalid_input_terminal_8(self, capfd, test_nand, mocker):
        mock_line = mocker.Mock()
        test_nand.connect_previous(mock_line, '8')
        out, err = capfd.readouterr()
        assert out == "Connection failed - invalid input terminal\n"
        
    def test_does_not_notify_valid_input_terminal_B(self, capfd, test_nand, mocker):
        mock_line = mocker.Mock()
        test_nand.connect_previous(mock_line, 'B')
        out, err = capfd.readouterr()
        assert out == ''
        
    def test_rejects_invalid_terminal_attribute(self, capfd, test_nand, mocker):
        mock_line = mocker.Mock()
        test_nand.connect_previous(mock_line, 'C')
        assert not hasattr(test_nand, 'in_connection_c')

class TestSignalReceipt:    
    def test_receives_high_input_signal_at_a(self, test_nand, mocker):
        mock_line = mocker.Mock()
        test_nand.connect_previous(mock_line, 'A')
        test_nand.receive_signal(mock_line, 'HIGH')
        assert test_nand.in_signal_a == 'HIGH'
        
    def test_receives_low_input_signal_at_a(self, test_nand, mocker):
        mock_line = mocker.Mock()
        test_nand.connect_previous(mock_line, 'A')
        test_nand.receive_signal(mock_line, 'LOW')
        assert test_nand.in_signal_a == 'LOW'
        
    def test_receives_high_input_signal_at_b(self, test_nand, mocker):
        mock_line = mocker.Mock()
        test_nand.connect_previous(mock_line, 'B')
        test_nand.receive_signal(mock_line, 'HIGH')
        assert test_nand.in_signal_b == 'HIGH'

    def test_receives_low_input_signal_at_b(self, test_nand, mocker):
        mock_line = mocker.Mock()
        test_nand.connect_previous(mock_line, 'B')
        test_nand.receive_signal(mock_line, 'LOW')
        assert test_nand.in_signal_b == 'LOW'
        
class TestPropagationAndLogic:  
    def test_gives_none_with_only_connection_a(self, test_nand, mocker):
        mock_line_a = mocker.Mock()
        test_nand.connect_previous(mock_line_a, 'A')
        test_nand.receive_signal(mock_line_a, 'LOW')
        assert test_nand.out_signal == None

    def test_gives_none_with_only_connection_b(self, test_nand, mocker):
        mock_line_b = mocker.Mock()
        test_nand.connect_previous(mock_line_b, 'B')
        test_nand.receive_signal(mock_line_b, 'LOW')
        assert test_nand.out_signal == None 
        
    def test_gives_none_with_only_signal_a(self, test_nand, mocker):
        mock_line_a = mocker.Mock()
        mock_line_b = mocker.Mock()
        test_nand.connect_previous(mock_line_a, 'A')
        test_nand.connect_previous(mock_line_b, 'B')
        test_nand.receive_signal(mock_line_a, 'LOW')
        assert test_nand.out_signal == None

    def test_gives_none_with_only_signal_b(self, test_nand, mocker):
        mock_line_a = mocker.Mock()
        mock_line_b = mocker.Mock()
        test_nand.connect_previous(mock_line_a, 'A')
        test_nand.connect_previous(mock_line_b, 'B')
        test_nand.receive_signal(mock_line_b, 'LOW')
        assert test_nand.out_signal == None 

    def test_outputs_high_for_low_low(self, test_nand, mocker):
        mock_line_a = mocker.Mock()
        mock_line_b = mocker.Mock()
        test_nand.connect_previous(mock_line_a, 'A')
        test_nand.connect_previous(mock_line_b, 'B')
        test_nand.receive_signal(mock_line_a, 'LOW')
        test_nand.receive_signal(mock_line_b, 'LOW')
        assert test_nand.out_signal == 'HIGH'   
        
    def test_outputs_high_for_low_high(self, test_nand, mocker):
        mock_line_a = mocker.Mock()
        mock_line_b = mocker.Mock()
        test_nand.connect_previous(mock_line_a, 'A')
        test_nand.connect_previous(mock_line_b, 'B')
        test_nand.receive_signal(mock_line_a, 'LOW')
        test_nand.receive_signal(mock_line_b, 'HIGH')
        assert test_nand.out_signal == 'HIGH'
        
    def test_outputs_high_for_high_low(self, test_nand, mocker):
        mock_line_a = mocker.Mock()
        mock_line_b = mocker.Mock()
        test_nand.connect_previous(mock_line_a, 'A')
        test_nand.connect_previous(mock_line_b, 'B')
        test_nand.receive_signal(mock_line_a, 'HIGH')
        test_nand.receive_signal(mock_line_b, 'LOW')
        assert test_nand.out_signal == 'HIGH'  
        
    def test_outputs_low_for_low_high(self, test_nand, mocker):
        mock_line_a = mocker.Mock()
        mock_line_b = mocker.Mock()
        test_nand.connect_previous(mock_line_a, 'A')
        test_nand.connect_previous(mock_line_b, 'B')
        test_nand.receive_signal(mock_line_a, 'HIGH')
        test_nand.receive_signal(mock_line_b, 'HIGH')
        assert test_nand.out_signal == 'LOW'   
        
class TestSignalTransmission:        
    def test_calls_receive_signal_on_next_with_low(self, test_nand, mocker):
        mock_line_a = mocker.Mock()
        mock_line_b = mocker.Mock()
        mock_line_x = mocker.Mock()
        test_nand.connect_previous(mock_line_a, 'A')
        test_nand.connect_previous(mock_line_b, 'B')
        test_nand.connect_next(mock_line_x)
        test_nand.receive_signal(mock_line_a, 'HIGH')
        test_nand.receive_signal(mock_line_b, 'HIGH')
        mock_line_x.receive_signal.assert_called_with('LOW')
        
    def test_calls_receive_signal_on_next_with_high(self, test_nand, mocker):
        mock_line_a = mocker.Mock()
        mock_line_b = mocker.Mock()
        mock_line_x = mocker.Mock()
        test_nand.connect_previous(mock_line_a, 'A')
        test_nand.connect_previous(mock_line_b, 'B')
        test_nand.connect_next(mock_line_x)
        test_nand.receive_signal(mock_line_a, 'HIGH')
        test_nand.receive_signal(mock_line_b, 'HIGH')
        mock_line_x.receive_signal.assert_called_with('LOW')
        
    def test_does_not_transmit_none(self, test_nand, mocker):
        mock_line_a = mocker.Mock()
        mock_line_b = mocker.Mock()
        mock_line_x = mocker.Mock()
        test_nand.connect_previous(mock_line_a, 'A')
        test_nand.connect_previous(mock_line_b, 'B')
        test_nand.connect_next(mock_line_x)
        test_nand.receive_signal(mock_line_a, 'HIGH')
        mock_line_x.receive_signal.assert_not_called()
