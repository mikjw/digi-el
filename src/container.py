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
        
    def add_input(self, n=1):
        try:
            if self.input_count + n <= self.input_count_limit:
                for i in range(n):
                    self.input_count += 1
                    label = chr(self.input_count + 64)
                    self.inputs[label] = {'component': None, 'signal': None}
            else:
                raise ValueError("Cannot add input - limit reached") 
        except ValueError as err:
            print(err)
            
    def add_output(self, n=1):
        try:
            if self.output_count + n <= self.output_count_limit:
                for i in range(n):
                    self.output_count += 1
                    label = chr(self.output_count + 64)
                    self.outputs[label] = {'component': None, 'signal': None}
            else:
                raise ValueError("Cannot add output - limit reached") 
        except ValueError as err:
            print(err)

