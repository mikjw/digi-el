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
