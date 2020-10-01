class Wire():
    def __init__(self):
        self.branch_count = 1
        self.in_connection = None
        self.in_signal = None
        
        self.out_connections = {
            'A': None
        }
        
        self.out_signal = None

    def connect_next(self, comp, terminal):
        try: 
            if (terminal in self.out_connections):
                self.out_connections[terminal] = comp
                self.out_connections[terminal].connect_previous(self, terminal)
            else: 
                raise ValueError("Connection failed - invalid terminal") 
        except ValueError as err:
            print(err)
                        
    def connect_previous(self, comp):
        self.in_connection = comp

    def receive_signal(self, signal):
        self.in_signal = signal
        self.__propagate_signal(signal)
        self.__transmit_signal(signal)
                
    def add_branch(self):
        try:
            if (self.branch_count < 10):
                self.branch_count += 1
                label = chr(self.branch_count + 64)
                self.out_connections[label] = None
            else:
                raise ValueError("Cannot add branch - limit reached") 
        except ValueError as err:
            print(err)
            
    def __propagate_signal(self, signal):
        self.out_signal = signal
            
    def __transmit_signal(self, signal):
        for key in self.out_connections:
            if (self.out_connections[key] != None): 
                self.out_connections[key].receive_signal(self.out_signal)
