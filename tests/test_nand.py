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
        test_nand.connect_next(mock_wire)
        assert test_nand.out_connection == mock_wire
        
    def test_connects_to_previous_comp_on_a(self, test_nand, mocker):
        mock_wire = mocker.Mock()
        test_nand.connect_previous(mock_wire, 'A')
        assert test_nand.in_connection_a == mock_wire
        
    def test_connects_to_previous_comp_on_b(self, test_nand, mocker):
        mock_wire = mocker.Mock()
        test_nand.connect_previous(mock_wire, 'B')
        assert test_nand.in_connection_b == mock_wire
        

# class TestConnection:
#     def test_connects_to_next_component_at_a(self, test_wire, mocker):
#         mock_wire = mocker.Mock()
#         test_wire.connect_next(mock_wire, 'A')
#         assert test_wire.out_connections['A'] == mock_wire
        
#     def test_connects_to_next_component_at_b(self, test_wire, mocker):
#         mock_wire = mocker.Mock()
#         test_wire.add_branch()
#         test_wire.connect_next(mock_wire, 'B')
#         assert test_wire.out_connections['B'] == mock_wire
        
#     def test_connects_to_previous_component(self, test_wire, mocker):
#         mock_wire = mocker.Mock()
#         test_wire.connect_previous(mock_wire)
#         assert test_wire.in_connection == mock_wire
        
#     def test_calls_connect_previous_on_next(self, test_wire, mocker):
#         mock_wire = mocker.Mock()
#         test_wire.connect_next(mock_wire, 'A')
#         mock_wire.connect_previous.assert_called_with(test_wire)
        
#     def test_raises_exception_invalid_terminal(self, capfd, test_wire, mocker):
#         mock_wire = mocker.Mock()
#         test_wire.connect_next(mock_wire, 'B')
#         out, err = capfd.readouterr()
#         assert out == "Connection failed - invalid terminal\n"

