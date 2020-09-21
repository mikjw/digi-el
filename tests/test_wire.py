import pytest
from src import wire

@pytest.fixture(autouse=True)   
def before_wire():
    test_wire = wire.Wire()
    return test_wire

@pytest.fixture(autouse=True)   
def before_wire_2():
    test_wire_2 = wire.Wire()
    return test_wire_2

class TestInitialization:
    def test_input_connection(self, before_wire):
        test_wire = before_wire
        assert test_wire.in_connnection == None

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
    def test_connects_to_next_component_at_a(self, before_wire, before_wire_2):
        test_wire = before_wire
        test_wire_2 = before_wire_2
        test_wire.connect_next(test_wire_2, 'A')
        assert test_wire.out_connections['A'] == test_wire_2
        
    def test_raises_exception_invalid_terminal(self, capfd, before_wire, before_wire_2):
        test_wire = before_wire
        test_wire_2 = before_wire_2
        test_wire.connect_next(test_wire_2, 'B')
        out, err = capfd.readouterr()
        assert out == "Connection failed - invalid terminal\n"
        
    def test_connects_to_next_component_at_b(self, before_wire, before_wire_2):
        test_wire = before_wire
        test_wire_2 = before_wire_2
        test_wire.add_branch()
        test_wire.connect_next(test_wire_2, 'B')
        assert test_wire.out_connections['B'] == test_wire_2
        
    def test_connects_to_previous_component(self, before_wire, before_wire_2):
        test_wire = before_wire
        test_wire_2 = before_wire_2
        test_wire.connect_next(test_wire_2, 'A')
        assert test_wire_2.in_conn == test_wire

class TestSignalReceipt:
    def test_receives_high_input_signal(self, before_wire):
        test_wire = before_wire
        test_wire.receive_signal('HIGH')
        assert test_wire.in_signal == 'HIGH'

    def test_receives_low_input_signal(self, before_wire):
        test_wire = before_wire
        test_wire.receive_signal('LOW')
        assert test_wire.in_signal == 'LOW'
        
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