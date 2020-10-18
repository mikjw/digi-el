class Container():
    def __init__(self):
        self.input_count = 1
        self.output_count = 1
        self.inputs = {'A': {'component': None, 'signal': None}}
        self.outputs = {'A': {'component': None, 'signal': None}}
        
    def add_input(self):
        if 'C' in self.inputs:
            self.inputs['D'] = {'component': None, 'signal': None}
        elif 'B' in self.inputs: 
            self.inputs['C'] = {'component': None, 'signal': None}
        else: 
            self.inputs['B'] = {'component': None, 'signal': None}      

