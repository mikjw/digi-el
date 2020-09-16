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
        assert test_wire.in_conn == None

    def test_output_connection(self, before_wire):
        test_wire = before_wire
        assert test_wire.out_conn == None

    def test_input_signal(self, before_wire):
        test_wire = before_wire
        assert test_wire.in_signal == None
        
    def test_output_signal(self, before_wire):
        test_wire = before_wire
        assert test_wire.out_signal == None

class TestConnection:
    def test_connects_to_next_component(self, before_wire, before_wire_2):
        test_wire = before_wire
        test_wire_2 = before_wire_2
        test_wire.connect_next(test_wire_2)
        assert test_wire.out_conn == test_wire_2

    def test_connects_to_previous_component(self, before_wire, before_wire_2):
        test_wire = before_wire
        test_wire_2 = before_wire_2
        test_wire.connect_next(test_wire_2)
        assert test_wire_2.in_conn == test_wire

class TestSignalReceipt:
    def test_receives_high_input_signal(self, before_wire):
        test_wire = before_wire
        test_wire.receive_signal('HIGH')
        assert test_wire.in_signal == 'HIGH'
