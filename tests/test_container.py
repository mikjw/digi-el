import pytest
from src import container

@pytest.fixture(autouse=True)   
def test_container():
    return container.Container()

class TestInitialization:
    def test_input(self, test_container):
        assert test_container.inputs['A'] == {'component': None, 'signal': None}
        
    def test_output(self, test_container):
        assert test_container.outputs['A'] == {'component': None, 'signal': None}
        
    def test_inits_with_input_count(self, test_container):
        assert test_container.input_count == 1
        
    def test_inits_with_output_count(self, test_container):
        assert test_container.output_count == 1

class TestInputCreation:
    def test_adds_input_b(self, test_container):
        test_container.add_input()
        assert test_container.inputs['B'] == {'component': None, 'signal': None}
        
    def test_adds_input_c(self, test_container):
        for i in range(2):
            test_container.add_input()
        assert test_container.inputs['C'] == {'component': None, 'signal': None}
     
    def test_adds_input_e(self, test_container):
        for i in range(9):
            test_container.add_input()
        assert test_container.inputs['J'] == {'component': None, 'signal': None}
        
    def test_increments_input_count_to_2(self, test_container):
        test_container.add_input()
        assert test_container.input_count == 2
        
    def test_increments_input_count_to_3(self, test_container):
        for i in range(2):
            test_container.add_input()
        assert test_container.input_count == 3
        
    def test_increments_input_count_to_9(self, test_container):
        for i in range(8):
            test_container.add_input()
        assert test_container.input_count == 9
        
    def test_limits_input_count_to_16(self, test_container):
        for i in range(17):
            test_container.add_input()
        assert test_container.input_count == 16
        
    def test_prints_input_count_limit_error(self, capfd, test_container):
        for i in range(16):
            test_container.add_input()
        out, err = capfd.readouterr()
        assert out == "Cannot add input - limit reached\n"
