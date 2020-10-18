class Container():
    def __init__(self):
        self.input_count = 1
        self.output_count = 1
        self.inputs = {'A': {'component': None, 'signal': None}}
        self.outputs = {'A': {'component': None, 'signal': None}}
        
    def add_input(self):
        if 'D' in self.inputs:
            self.inputs['E'] = {'component': None, 'signal': None}
            self.input_count = 5
        elif 'C' in self.inputs:
            self.inputs['D'] = {'component': None, 'signal': None}
            self.input_count = 4  
        elif 'B' in self.inputs:
            self.inputs['C'] = {'component': None, 'signal': None}
            self.input_count = 3  
        else:
            self.inputs['B'] = {'component': None, 'signal': None} 
            self.input_count = 2

