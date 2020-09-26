import pytest
from src import nand

@pytest.fixture(autouse=True)   
def before_nand():
    return nand.Nand()

class TestInitialization:
    def test_input_connection_a(self, before_nand):
        test_nand = before_nand
        assert test_nand.in_connection_a == None
        
    def test_input_connection_b(self, before_nand):
        test_nand = before_nand
        assert test_nand.in_connection_b == None
        
    def test_input_signal_a(self, before_nand):
        test_nand = before_nand
        assert test_nand.in_signal_a == None
        
    def test_input_signal_b(self, before_nand):
        test_nand = before_nand
        assert test_nand.in_signal_b == None
        
    def test_output_connection(self, before_nand):
        test_nand = before_nand
        assert test_nand.out_connection == None
        
    def test_output_signal(self, before_nand):
        test_nand = before_nand
        assert test_nand.out_signal == None

