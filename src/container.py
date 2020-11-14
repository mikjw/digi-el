class Container():
    def __init__(self, inputs=1, outputs=1):
        self.input_count_limit = 13
        self.output_count_limit = 13
        self.input_count = 0
        self.output_count = 0
        self.internal_inputs = {}
        self.outputs = {}
    
        self.add_input(inputs)
        self.add_output(outputs)
        
    def add_input(self, number_to_add=1):
        try:
            if self.input_count + number_to_add > self.input_count_limit:
                raise ValueError("Cannot add input - limit reached") 
            else:
                for i in range(number_to_add):
                    self.input_count += 1
                    label = chr(self.input_count + 64)
                    self.internal_inputs[label] = {'component': None, 'signal': None}
        except ValueError as err:
            print(err)
            
    def add_output(self, number_to_add=1):
        try:
            if self.output_count + number_to_add > self.output_count_limit:
                raise ValueError("Cannot add output - limit reached") 
            else:
                for i in range(number_to_add):
                    self.output_count += 1
                    label = chr(- self.output_count + 91)
                    self.outputs[label] = {'component': None, 'signal': None}
        except ValueError as err:
            print(err)
            
    def connect_within(self, component, terminal):
        try:
            if terminal not in self.internal_inputs:
                raise ValueError("Connection failed - invalid input terminal on container")
            else:
                self.internal_inputs[terminal]['component'] = component
                self.internal_inputs[terminal]['component'].connect_previous(self)
        except ValueError as err:
            print(err)
        
    def connect_previous(self, component, terminal):
        self.outputs[terminal]['component'] = component

