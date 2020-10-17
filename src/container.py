class Container():
    def __init__(self):
        self.input_count = 1
        self.output_count = 1
        self.inputs = {'A': {'component': None, 'signal': None}}
        self.outputs = {'A': {'component': None, 'signal': None}}
        
    def add_input(self):
        self.inputs['B'] = {'component': None, 'signal': None}

