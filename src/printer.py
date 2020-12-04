class Printer():
    def __init__(self):
        self.input_count = 0
        self.inputs = {}

    def add_input(self):
        self.inputs['A'] = {'component': None, 'signal': None}
        self.inputs['B'] = {'component': None, 'signal': None}
        self.inputs['C'] = {'component': None, 'signal': None}
        self.input_count += 1


