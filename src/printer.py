class Printer():
    def __init__(self):
        self.input_count = 0
        self.inputs = {}

    def add_input(self):
        self.input_count += 1
        if self.input_count == 1:
            self.inputs['A'] = {'component': None, 'signal': None}
        elif self.input_count == 2:
            self.inputs['B'] = {'component': None, 'signal': None}
        self.inputs['C'] = {'component': None, 'signal': None}



