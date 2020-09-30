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
        mock_wire = mocker.Mock()
        test_nand.connect_next(mock_wire, 'A')
        assert test_nand.out_connection == mock_wire
        
    def test_connects_to_previous_comp_on_a(self, test_nand, mocker):
        mock_wire = mocker.Mock()
        test_nand.connect_previous(mock_wire, 'A')
        assert test_nand.in_connection_a == mock_wire
        
    def test_connects_to_previous_comp_on_b(self, test_nand, mocker):
        mock_wire = mocker.Mock()
        test_nand.connect_previous(mock_wire, 'B')
        assert test_nand.in_connection_b == mock_wire
                
    def test_calls_connect_previous_on_next_comp(self, test_nand, mocker):
        mock_wire = mocker.Mock()
        test_nand.connect_next(mock_wire, 'A')
        mock_wire.connect_previous.assert_called_with(test_nand, 'A')
        
    def test_notifies_invalid_input_terminal_C(self, capfd, test_nand, mocker):
        mock_wire = mocker.Mock()
        test_nand.connect_previous(mock_wire, 'C')
        out, err = capfd.readouterr()
        assert out == "Connection failed - invalid input terminal\n"
        
    def test_notifies_invalid_input_terminal_8(self, capfd, test_nand, mocker):
        mock_wire = mocker.Mock()
        test_nand.connect_previous(mock_wire, '8')
        out, err = capfd.readouterr()
        assert out == "Connection failed - invalid input terminal\n"
        
    def test_does_not_notify_valid_input_terminal_B(self, capfd, test_nand, mocker):
        mock_wire = mocker.Mock()
        test_nand.connect_previous(mock_wire, 'B')
        out, err = capfd.readouterr()
        assert out != "Connection failed - invalid input terminal\n"
        
    def test_rejects_invalid_terminal_attribute(self, capfd, test_nand, mocker):
        mock_wire = mocker.Mock()
        test_nand.connect_previous(mock_wire, 'C')
        assert not hasattr(test_nand, 'in_connection_c')

class TestSignalReceipt:    
    def test_receives_high_input_signal_at_a(self, test_nand, mocker):
        mock_wire = mocker.Mock()
        test_nand.connect_previous(mock_wire, 'A')
        test_nand.receive_signal(mock_wire, 'HIGH')
        assert test_nand.in_signal_a == 'HIGH'
        
    def test_receives_low_input_signal_at_a(self, test_nand, mocker):
        mock_wire = mocker.Mock()
        test_nand.connect_previous(mock_wire, 'A')
        test_nand.receive_signal(mock_wire, 'LOW')
        assert test_nand.in_signal_a == 'LOW'
        
    def test_receives_high_input_signal_at_b(self, test_nand, mocker):
        mock_wire = mocker.Mock()
        test_nand.connect_previous(mock_wire, 'B')
        test_nand.receive_signal(mock_wire, 'HIGH')
        assert test_nand.in_signal_b == 'HIGH'

    def test_receives_low_input_signal_at_b(self, test_nand, mocker):
        mock_wire = mocker.Mock()
        test_nand.connect_previous(mock_wire, 'B')
        test_nand.receive_signal(mock_wire, 'LOW')
        assert test_nand.in_signal_b == 'LOW'
