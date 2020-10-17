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
        test_container.add_input()
        test_container.add_input()
        assert test_container.inputs['C'] == {'component': None, 'signal': None}
     