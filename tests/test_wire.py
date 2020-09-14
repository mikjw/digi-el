import pytest
from src import wire

@pytest.fixture(autouse=True)   
def before_wire():
    test_wire = wire.Wire()
    return test_wire

class TestInitialization:
    def testInput(self, before_wire):
        test_wire = before_wire
        assert test_wire.in_conn == None

    def testOutput(self, before_wire):
        test_wire = before_wire
        assert test_wire.out_conn == None