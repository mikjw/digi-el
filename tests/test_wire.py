import pytest
from src import wire

@pytest.fixture(autouse=True)   
def before_wire():
    return wire.Wire()

class TestInitialization:
    def test_input_connection(self, before_wire):
        test_wire = before_wire
        assert test_wire.in_connection == None

    def test_input_signal(self, before_wire):
        test_wire = before_wire
        assert test_wire.in_signal == None
                 
    def test_output_connection(self, before_wire):
        test_wire = before_wire
        assert test_wire.out_connections['A'] == None
        
    def test_output_signal(self, before_wire):
        test_wire = before_wire
        assert test_wire.out_signals['A'] == None
        
    def test_has_branch_count(self, before_wire):
        test_wire = before_wire
        assert hasattr(test_wire, 'branch_count')
        
    def test_branch_count_is_1(self, before_wire):
        test_wire = before_wire
        assert test_wire.branch_count == 1

class TestConnection:
    def test_connects_to_next_component_at_a(self, before_wire, mocker):
        test_wire = before_wire
        mock_wire = mocker.Mock()
        test_wire.connect_next(mock_wire, 'A')
        assert test_wire.out_connections['A'] == mock_wire
        
    def test_connects_to_next_component_at_b(self, before_wire, mocker):
        test_wire = before_wire
        mock_wire = mocker.Mock()
        test_wire.add_branch()
        test_wire.connect_next(mock_wire, 'B')
        assert test_wire.out_connections['B'] == mock_wire
        
    def test_connects_to_previous_component(self, before_wire, mocker):
        test_wire = before_wire
        mock_wire = mocker.Mock()
        test_wire.connect_previous(mock_wire)
        assert test_wire.in_connection == mock_wire
        
    def test_calls_connect_previous_on_next(self, before_wire, mocker):
        test_wire = before_wire
        mock_wire = mocker.Mock()
        test_wire.connect_next(mock_wire, 'A')
        mock_wire.connect_previous.assert_called_with(test_wire)
        
    def test_raises_exception_invalid_terminal(self, capfd, before_wire, mocker):
        test_wire = before_wire
        mock_wire = mocker.Mock()
        test_wire.connect_next(mock_wire, 'B')
        out, err = capfd.readouterr()
        assert out == "Connection failed - invalid terminal\n"

class TestSignalReceipt:
    def test_receives_high_input_signal(self, before_wire):
        test_wire = before_wire
        test_wire.receive_signal('HIGH')
        assert test_wire.in_signal == 'HIGH'

    def test_receives_low_input_signal(self, before_wire):
        test_wire = before_wire
        test_wire.receive_signal('LOW')
        assert test_wire.in_signal == 'LOW'
        
class TestSignalPropagation:
    def test_one_out_signal_low(self, before_wire):
        test_wire = before_wire
        test_wire.receive_signal('LOW')
        assert test_wire.out_signals['A'] == 'LOW'
        
    def test_one_out_signal_high(self, before_wire):
        test_wire = before_wire
        test_wire.receive_signal('HIGH')
        assert test_wire.out_signals['A'] == 'HIGH'
        
    def test_two_out_signal_low(self, before_wire):
        test_wire = before_wire
        test_wire.add_branch()
        test_wire.receive_signal('LOW')
        assert test_wire.out_signals['A'] == 'LOW'
        assert test_wire.out_signals['B'] == 'LOW'
    
    def test_three_out_signal_high(self, before_wire):
        test_wire = before_wire
        for i in range(2):
            test_wire.add_branch()
        test_wire.receive_signal('HIGH')
        assert test_wire.out_signals['A'] == 'HIGH'
        assert test_wire.out_signals['B'] == 'HIGH'
        assert test_wire.out_signals['C'] == 'HIGH'
        
class TestSignalTransmission:        
    def test_calls_receive_signal_on_next_with_high(self, before_wire, mocker):
        test_wire = before_wire
        mock_wire = mocker.Mock()
        test_wire.connect_next(mock_wire, 'A')
        test_wire.receive_signal('HIGH')
        mock_wire.receive_signal.assert_called_with('HIGH')
        
    def test_calls_receive_signal_on_next_with_low(self, before_wire, mocker):
        test_wire = before_wire
        mock_wire = mocker.Mock()
        test_wire.connect_next(mock_wire, 'A')
        test_wire.receive_signal('LOW')
        mock_wire.receive_signal.assert_called_with('LOW')
        
class TestBranchCreation:
    def test_adds_branch_b_conn(self, before_wire):
        test_wire = before_wire
        test_wire.add_branch()
        assert test_wire.out_connections['B'] == None
        
    def test_adds_branch_c_conn(self, before_wire):
        test_wire = before_wire
        for i in range(2):
            test_wire.add_branch()
        assert test_wire.out_connections['C'] == None
        
    def test_adds_branch_j_conn(self, before_wire):
        test_wire = before_wire
        for i in range(9):
            test_wire.add_branch()
        assert test_wire.out_connections['J'] == None
        
    def test_adds_branch_b_signal(self, before_wire):
        test_wire = before_wire
        test_wire.add_branch()
        assert test_wire.out_signals['B'] == None
        
    def test_increments_branch_count(self, before_wire):
        test_wire = before_wire
        test_wire.add_branch()
        assert test_wire.branch_count == 2
        
    def test_twice_increments_branch_count(self, before_wire):
        test_wire = before_wire
        for i in range(2):
            test_wire.add_branch()
        assert test_wire.branch_count == 3
        
    def test_increments_branch_count_9_times(self, before_wire):
        test_wire = before_wire
        for i in range(9):
            test_wire.add_branch()
        assert test_wire.branch_count == 10
        
    def test_limits_branch_count_to_10(self, before_wire):
        test_wire = before_wire
        for i in range(11):
            test_wire.add_branch()
        assert test_wire.branch_count == 10
    
    def test_prints_branch_limit_error(self, capfd, before_wire):
        test_wire = before_wire
        for i in range(10):
            test_wire.add_branch()
        out, err = capfd.readouterr()
        assert out == "Cannot add branch - limit reached\n"
        