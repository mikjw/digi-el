class Nand():
    def __init__(self):
        self.in_connection_a = None
        self.in_connection_b = None
        self.in_signal_a = None
        self.in_signal_b = None
        self.out_connection = None
        self.out_signal = None
        
    def connect_next(self, comp):
        self.out_connection = comp
        self.out_connection.connect_previous(self)
        
    def connect_previous(self, comp, terminal):
        try: 
            if terminal != 'A' and terminal != 'B':
                raise ValueError("Connection failed - invalid input terminal")
            else:
                lowercase_label = chr(ord(terminal) + 32)
                setattr(self, f'in_connection_{lowercase_label}', comp)
        except ValueError as err:
            print(err)
            
    def receive_signal(self, comp, signal):
        self.__assign_input(comp, signal)
        print(str(self) + ": received " + str(signal) + " from " + str(comp))
        self.__perform_logic()
        if self.out_connection is not None and self.out_signal is not None:
            self.__transmit_signal()

    def __assign_input(self, comp, signal):
        if self.in_connection_a == comp and self.in_signal_a == None:
            self.in_signal_a = signal
        elif self.in_connection_b == comp and self.in_signal_b == None:
            self.in_signal_b = signal
            
    def __perform_logic(self):
        if ((self.in_signal_a == 'LOW' and self.in_signal_b == 'LOW') or 
            (self.in_signal_a == 'LOW' and self.in_signal_b == 'HIGH') or 
            (self.in_signal_a == 'HIGH' and self.in_signal_b == 'LOW')):
                self.out_signal = 'HIGH'
        elif self.in_signal_a == 'HIGH' and self.in_signal_b == 'HIGH': 
                self.out_signal = 'LOW'
                
    def __transmit_signal(self):
        self.out_connection.receive_signal(self.out_signal)
