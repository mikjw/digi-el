import pytest
from src import wire

@pytest.fixture(autouse=True)   
def test_wire():
    return wire.Wire()

class TestInitialization:
    def test_input_connection(self, test_wire):
        assert test_wire.in_connection == None

    def test_input_signal(self, test_wire):
        assert test_wire.in_signal == None
                 
    def test_output_connection(self, test_wire):
        assert test_wire.out_connections['A'] == None
        
    def test_output_signal(self, test_wire):
        assert test_wire.out_signal == None
        
    def test_has_branch_count(self, test_wire):
        assert hasattr(test_wire, 'branch_count')
        
    def test_branch_count_is_1(self, test_wire):
        assert test_wire.branch_count == 1
        
    def test_initializes_with_branches(self):
        test_wire_2 = wire.Wire(5)
        assert test_wire_2.out_connections["E"] == None

class TestConnection:
    def test_connects_to_next_component_at_a(self, test_wire, mocker):
        mock_component = mocker.Mock()
        test_wire.connect_next(mock_component, 'A', 'A')
        assert test_wire.out_connections['A'] == mock_component
        
    def test_connects_to_next_component_at_b(self, test_wire, mocker):
        mock_component = mocker.Mock()
        test_wire.add_branch()
        test_wire.connect_next(mock_component, 'B', 'A')
        assert test_wire.out_connections['B'] == mock_component
        
    def test_connects_to_previous_component(self, test_wire, mocker):
        mock_component = mocker.Mock()
        test_wire.connect_previous(mock_component)
        assert test_wire.in_connection == mock_component
        
    def test_calls_connect_previous_on_next_with_a(self, test_wire, mocker):
        mock_component = mocker.Mock()
        test_wire.connect_next(mock_component, 'A', 'A')
        mock_component.connect_previous.assert_called_with(test_wire, 'A')
        
    def test_calls_connect_previous_on_next_with_a(self, test_wire, mocker):
        mock_component = mocker.Mock()
        test_wire.connect_next(mock_component, 'A', 'B')
        mock_component.connect_previous.assert_called_with(test_wire, 'B')
        
    def test_notifies_invalid_terminal(self, capfd, test_wire, mocker):
        mock_component = mocker.Mock()
        test_wire.connect_next(mock_component, 'B', 'A')
        out, err = capfd.readouterr()
        assert out == "Connection failed - invalid terminal\n"

class TestSignalReceipt:
    def test_receives_high_input_signal(self, test_wire):
        test_wire.receive_signal('HIGH')
        assert test_wire.in_signal == 'HIGH'

    def test_receives_low_input_signal(self, test_wire):
        test_wire.receive_signal('LOW')
        assert test_wire.in_signal == 'LOW'
        
class TestSignalPropagation:
    def test_one_out_signal_low(self, test_wire):
        test_wire.receive_signal('LOW')
        assert test_wire.out_signal == 'LOW'
        
    def test_one_out_signal_high(self, test_wire):
        test_wire.receive_signal('HIGH')
        assert test_wire.out_signal == 'HIGH'
        
class TestSignalTransmission:        
    def test_calls_receive_signal_on_next_with_high(self, test_wire, mocker):
        mock_component = mocker.Mock()
        test_wire.connect_next(mock_component, 'A', 'A')
        test_wire.receive_signal('HIGH')
        mock_component.receive_signal.assert_called_with(test_wire, 'HIGH')
        
    def test_calls_receive_signal_on_next_with_low(self, test_wire, mocker):
        mock_component = mocker.Mock()
        test_wire.connect_next(mock_component, 'A', 'A')
        test_wire.receive_signal('LOW')
        mock_component.receive_signal.assert_called_with(test_wire, 'LOW')
        
class TestBranchCreation:
    def test_adds_branch_b_conn(self, test_wire):
        test_wire.add_branch()
        assert test_wire.out_connections['B'] == None
        
    def test_adds_branch_c_conn(self, test_wire):
        for i in range(2):
            test_wire.add_branch()
        assert test_wire.out_connections['C'] == None
        
    def test_adds_branch_j_conn(self, test_wire):
        for i in range(9):
            test_wire.add_branch()
        assert test_wire.out_connections['J'] == None
        
    def test_increments_branch_count(self, test_wire):
        test_wire.add_branch()
        assert test_wire.branch_count == 2
        
    def test_twice_increments_branch_count(self, test_wire):
        for i in range(2):
            test_wire.add_branch()
        assert test_wire.branch_count == 3
        
    def test_increments_branch_count_9_times(self, test_wire):
        for i in range(9):
            test_wire.add_branch()
        assert test_wire.branch_count == 10
        
    def test_limits_branch_count_to_10(self, test_wire):
        for i in range(11):
            test_wire.add_branch()
        assert test_wire.branch_count == 10
    
    def test_prints_branch_limit_error(self, capfd, test_wire):
        for i in range(10):
            test_wire.add_branch()
        out, err = capfd.readouterr()
        assert out == "Cannot add branch - limit reached\n"
        
    def test_creates_n_branches(self, test_wire):
        test_wire.add_branch(4)
        assert test_wire.branch_count == 5
        