import pytest
from src import container

@pytest.fixture(autouse=True)   
def test_container():
    return container.Container()

class TestInitialization:
    def test_input_connection(self, test_container):
        assert test_container.inputs['A'] == {'component': None, 'signal': None}
