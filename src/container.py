class Container():
    def __init__(self, inputs=1, outputs=1):
        self.input_count_limit = 13
        self.output_count_limit = 13
        self.input_count = 0
        self.output_count = 0
        self.inputs = {}
        self.outputs = {}
    
        self.add_input(inputs)
        self.add_output(outputs)
        
    def add_input(self, number_to_add=1):
        try:
            if self.input_count + number_to_add > self.input_count_limit:
                raise ValueError("Cannot add input - limit reached") 
            else:
                for i in range(number_to_add):
                    self.input_count += 1
                    label = chr(self.input_count + 64)
                    self.inputs[label] = {'inner_component': None, 'outer_component': None, 'signal': None}
        except ValueError as err:
            print(err)
            
    def add_output(self, number_to_add=1):
        try:
            if self.output_count + number_to_add > self.output_count_limit:
                raise ValueError("Cannot add output - limit reached") 
            else:
                for i in range(number_to_add):
                    self.output_count += 1
                    label = chr(- self.output_count + 91)
                    self.outputs[label] = {'inner_component': None, 'outer_component': None, 'signal': None}
        except ValueError as err:
            print(err)
            
    def connect_within(self, component, terminal):
        try:
            if terminal not in self.inputs:
                raise ValueError("Connection failed - invalid input terminal on container")
            else:
                self.inputs[terminal]['inner_component'] = component
                self.inputs[terminal]['inner_component'].connect_previous(self)
        except ValueError as err:
            print(err)
        
    def connect_previous(self, component, terminal):
        try:
            if terminal not in self.outputs and terminal not in self.inputs:
                raise ValueError("Connection failed - invalid terminal on container")
            elif self.__is_input(terminal):
                self.inputs[terminal]['outer_component'] = component
            else:
                self.outputs[terminal]['inner_component'] = component
        except ValueError as err:
            print(err)
        
    def connect_next(self, component, terminal):
        try:
            if terminal not in self.outputs:
                raise ValueError("Connection failed - invalid terminal on container")
            else:
                self.outputs[terminal]['outer_component'] = component
                self.outputs[terminal]['outer_component'].connect_previous(self)
        except ValueError as err:
            print(err)

    def receive_signal(self, component, signal):    
        for key, value in self.inputs.items():
            if value['outer_component'] == component:
                value['signal'] = signal
                self.__transmit(key)
        for key, value in self.outputs.items():
            if value['inner_component'] == component:
                value['signal'] = signal
                self.__transmit(key)

    def __transmit(self, terminal):
        if self.__is_input(terminal):
            self.inputs[terminal]['inner_component'].receive_signal(self.inputs[terminal]['signal'])
        else:
            self.outputs[terminal]['outer_component'].receive_signal(self.outputs[terminal]['signal'])

    def __is_input(self, terminal):
        return 65 <= ord(terminal) <= 77