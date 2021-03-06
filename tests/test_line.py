import pytest
from src import line

@pytest.fixture(autouse=True)   
def test_line():
    return line.Line()

class TestInitialization:
    def test_input_connection(self, test_line):
        assert test_line.in_connection == None

    def test_input_signal(self, test_line):
        assert test_line.in_signal == None
                 
    def test_output_connection(self, test_line):
        assert test_line.out_connections['A'] == None
        
    def test_output_signal(self, test_line):
        assert test_line.out_signal == None
        
    def test_has_branch_count(self, test_line):
        assert hasattr(test_line, 'branch_count')
        
    def test_branch_count_is_1(self, test_line):
        assert test_line.branch_count == 1
        
    def test_initializes_with_branches(self):
        test_line_2 = line.Line(5)
        assert test_line_2.out_connections["E"] == None

class TestConnection:
    def test_connects_to_next_component_at_a(self, test_line, mocker):
        mock_component = mocker.Mock()
        test_line.connect_next(mock_component, 'A', 'A')
        assert test_line.out_connections['A'] == mock_component
        
    def test_connects_to_next_component_at_b(self, test_line, mocker):
        mock_component = mocker.Mock()
        test_line.add_branch()
        test_line.connect_next(mock_component, 'B', 'A')
        assert test_line.out_connections['B'] == mock_component
        
    def test_connects_to_previous_component(self, test_line, mocker):
        mock_component = mocker.Mock()
        test_line.connect_previous(mock_component)
        assert test_line.in_connection == mock_component
        
    def test_calls_connect_previous_on_next_with_a(self, test_line, mocker):
        mock_component = mocker.Mock()
        test_line.connect_next(mock_component, 'A', 'A')
        mock_component.connect_previous.assert_called_with(test_line, 'A')
        
    def test_calls_connect_previous_on_next_with_b(self, test_line, mocker):
        mock_component = mocker.Mock()
        test_line.connect_next(mock_component, 'A', 'B')
        mock_component.connect_previous.assert_called_with(test_line, 'B')
        
    def test_notifies_invalid_terminal(self, capfd, test_line, mocker):
        mock_component = mocker.Mock()
        test_line.connect_next(mock_component, 'B', 'A')
        out, err = capfd.readouterr()
        assert out == "Connection failed - invalid terminal\n"

class TestSignalReceipt:
    def test_receives_high_input_signal(self, test_line):
        test_line.receive_signal('HIGH')
        assert test_line.in_signal == 'HIGH'

    def test_receives_low_input_signal(self, test_line):
        test_line.receive_signal('LOW')
        assert test_line.in_signal == 'LOW'
        
class TestSignalPropagation:
    def test_one_out_signal_low(self, test_line):
        test_line.receive_signal('LOW')
        assert test_line.out_signal == 'LOW'
        
    def test_one_out_signal_high(self, test_line):
        test_line.receive_signal('HIGH')
        assert test_line.out_signal == 'HIGH'
        
class TestSignalTransmission:        
    def test_calls_receive_signal_on_next_with_high(self, test_line, mocker):
        mock_component = mocker.Mock()
        test_line.connect_next(mock_component, 'A', 'A')
        test_line.receive_signal('HIGH')
        mock_component.receive_signal.assert_called_with(test_line, 'HIGH')
        
    def test_calls_receive_signal_on_next_with_low(self, test_line, mocker):
        mock_component = mocker.Mock()
        test_line.connect_next(mock_component, 'A', 'A')
        test_line.receive_signal('LOW')
        mock_component.receive_signal.assert_called_with(test_line, 'LOW')
        
class TestBranchCreation:
    def test_adds_branch_b_conn(self, test_line):
        test_line.add_branch()
        assert test_line.out_connections['B'] == None
        
    def test_adds_branch_c_conn(self, test_line):
        test_line.add_branch(2)
        assert test_line.out_connections['C'] == None
        
    def test_adds_branch_j_conn(self, test_line):
        test_line.add_branch(9)
        assert test_line.out_connections['J'] == None
        
    def test_increments_branch_count(self, test_line):
        test_line.add_branch()
        assert test_line.branch_count == 2
        
    def test_twice_increments_branch_count(self, test_line):
        test_line.add_branch(2)
        assert test_line.branch_count == 3
        
    def test_increments_branch_count_9_times(self, test_line):
        test_line.add_branch(9)
        assert test_line.branch_count == 10
        
    def test_limits_branch_count_to_10(self, test_line):
        test_line.add_branch(9)
        test_line.add_branch()
        assert test_line.branch_count == 10
    
    def test_prints_branch_limit_error(self, capfd, test_line):
        test_line.add_branch(10)
        out, err = capfd.readouterr()
        assert out == "Cannot add branch - limit reached\n"

        