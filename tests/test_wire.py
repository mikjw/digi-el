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
    def testInput(self, before_wire):
        test_wire = before_wire
        assert test_wire.in_conn == None

    def testOutput(self, before_wire):
        test_wire = before_wire
        assert test_wire.out_conn == None

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