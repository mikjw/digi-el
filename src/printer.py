class Printer():
    def __init__(self, source_component=None):
        self.source_component = source_component
        self.input_count = 0
        self.inputs = {}

        if self.source_component is not None:
            self.add_input(len(self.source_component.get_outputs()))

    def add_input(self, number_to_add=1):
        for i in range(number_to_add):
            self.input_count += 1
            label = chr(self.input_count + 64)
            self.inputs[label] = {'component': None, 'signal': None}


