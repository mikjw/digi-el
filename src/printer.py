from .line import Line

class Printer():
    def __init__(self, source_component=None):
        self.source_component = source_component
        self.input_count = 0
        self.inputs = {}

        if self.source_component is not None:
            self.add_input(len(self.source_component.get_outputs()))
            self.connect_source()

    def add_input(self, number_to_add=1):
        for i in range(number_to_add):
            self.input_count += 1
            label = chr(self.input_count + 64)
            self.inputs[label] = {'component': None, 'signal': None}

    def connect_previous(self, comp, terminal):
        self.inputs[terminal]['component'] = comp

    def connect_source(self):
        for i, v in enumerate(self.inputs):
            line = Line()
            out_terminal = in_terminal = chr(i + 65)
            self.inputs[in_terminal]['component'] = line
            self.inputs[in_terminal]['component'].connect_next(self, out_terminal, in_terminal)

    def receive_signal(self, component, signal):
        for key, value in self.inputs.items():
            if value['component'] == component:
                value['signal'] = signal

