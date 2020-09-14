import pytest
import wire

class TestInitialization:
    def testInput(self):
        test_wire = wire.Wire()
        assert test_wire.end_a_conn == None