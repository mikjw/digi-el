class Container():
    def __init__(self):
        self.input_count_limit = 16
        self.input_count = 1
        self.output_count = 1
        self.inputs = {'A': {'component': None, 'signal': None}}
        self.outputs = {'A': {'component': None, 'signal': None}}
        
    def add_input(self):
        try:
            if self.input_count < self.input_count_limit:
                self.input_count += 1
                label = chr(self.input_count + 64)
                self.inputs[label] = {'component': None, 'signal': None}
            else:
                raise ValueError("Cannot add input - limit reached") 
        except ValueError as err:
            print(err)

