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
        
    def test_increments_5_inputs_on_initialization(self):
        test_container_2 = container.Container(5)
        assert test_container_2.input_count == 5
        
    def test_creates_5_inputs_on_initialization(self):
        test_container_2 = container.Container(5)
        assert 'E' in test_container_2.inputs
        
    def test_increments_15_inputs_on_initialization(self):
        test_container_2 = container.Container(15)
        assert test_container_2.input_count == 15
        
    def test_creates_15_inputs_on_initialization(self):
        test_container_2 = container.Container(15)
        assert 'O' in test_container_2.inputs

class TestInputCreation:
    def test_adds_input_b(self, test_container):
        test_container.add_input()
        assert test_container.inputs['B'] == {'component': None, 'signal': None}
        
    def test_adds_input_c(self, test_container):
        test_container.add_input(2)
        assert test_container.inputs['C'] == {'component': None, 'signal': None}
     
    def test_adds_input_e(self, test_container):
        test_container.add_input(9)
        assert test_container.inputs['J'] == {'component': None, 'signal': None}
        
    def test_increments_input_count_to_2(self, test_container):
        test_container.add_input()
        assert test_container.input_count == 2
        
    def test_increments_input_count_to_3(self, test_container):
        test_container.add_input(2)
        assert test_container.input_count == 3
        
    def test_increments_input_count_to_9(self, test_container):
        test_container.add_input(8)
        assert test_container.input_count == 9
        
    def test_limits_input_count_to_16(self, test_container):
        test_container.add_input(15)
        test_container.add_input()
        assert test_container.input_count == 16
        
    def test_prints_input_count_limit_error(self, capfd, test_container):
        test_container.add_input(16)
        out, err = capfd.readouterr()
        assert out == "Cannot add input - limit reached\n"

class TestOutputCreation:
    def test_adds_output_b(self, test_container):
        test_container.add_output()
        assert test_container.outputs['B'] == {'component': None, 'signal': None}
        
    def test_adds_output_c(self, test_container):
        test_container.add_output(2)
        assert test_container.outputs['C'] == {'component': None, 'signal': None}
     
    def test_adds_output_e(self, test_container):
        test_container.add_output(9)
        assert test_container.outputs['J'] == {'component': None, 'signal': None}
        
    def test_increments_output_count_to_2(self, test_container):
        test_container.add_output()
        assert test_container.output_count == 2
        
    def test_increments_output_count_to_3(self, test_container):
        test_container.add_output(2)
        assert test_container.output_count == 3
        
    def test_increments_output_count_to_9(self, test_container):
        test_container.add_output(8)
        assert test_container.output_count == 9
        
    def test_limits_output_count_to_16(self, test_container):
        test_container.add_output(15)
        test_container.add_output()
        assert test_container.output_count == 16
        
    def test_prints_output_count_limit_error(self, capfd, test_container):
        test_container.add_output(16)
        out, err = capfd.readouterr()
        assert out == "Cannot add output - limit reached\n"

class TestConnection:
    def test_connects_to_component_at_input_a(self, test_container, mocker):
        test_wire = mocker.Mock()
        test_container.connect_within(test_wire, 'A')
        assert test_container.inputs['A']['component'] == test_wire
        
    def test_connects_to_component_at_input_b(self, test_container, mocker):
        test_wire = mocker.Mock()
        test_container.add_input()
        test_container.connect_within(test_wire, 'B')
        assert test_container.inputs['B']['component'] == test_wire
     
    def test_calls_connect_previous_on_comp(self, test_container, mocker):
        mock_wire = mocker.Mock()
        test_container.connect_within(mock_wire, 'A')
        mock_wire.connect_previous.assert_called_with(test_container)
