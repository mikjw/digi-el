class Printer():
    def __init__(self, source_component):
        self.source_component = source_component
        self.input_count = 0
        self.inputs = {}

    def add_input(self):
        self.input_count += 1
        label = chr(self.input_count + 64)
        self.inputs[label] = {'component': None, 'signal': None}


