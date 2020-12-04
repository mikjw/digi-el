import pytest
from src import printer

@pytest.fixture(autouse=True)   
def test_printer():
    return printer.Printer()

class TestInitialization:
    def test_has_empty_inputs_dict(self, test_printer):
        assert test_printer.inputs == {}

    def test_has_input_count(self, test_printer):
        assert test_printer.input_count == 0


