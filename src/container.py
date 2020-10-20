class Container():
    def __init__(self, inputs=1, outputs=1):
        self.input_count_limit = 16
        self.output_count_limit = 16
        self.input_count = 0
        self.output_count = 0
        self.inputs = {}
        self.outputs = {}
    
        self.add_input(inputs)
        self.add_output(outputs)
        
    def add_input(self, number_to_add=1):
        try:
            if self.input_count + number_to_add <= self.input_count_limit:
                for i in range(number_to_add):
                    self.input_count += 1
                    label = chr(self.input_count + 64)
                    self.inputs[label] = {'component': None, 'signal': None}
            else:
                raise ValueError("Cannot add input - limit reached") 
        except ValueError as err:
            print(err)
            
    def add_output(self, number_to_add=1):
        try:
            if self.output_count + number_to_add <= self.output_count_limit:
                for i in range(number_to_add):
                    self.output_count += 1
                    label = chr(self.output_count + 64)
                    self.outputs[label] = {'component': None, 'signal': None}
            else:
                raise ValueError("Cannot add output - limit reached") 
        except ValueError as err:
            print(err)
            
    def connect_next(self, component, terminal):
        self.inputs[terminal]['component'] = component
