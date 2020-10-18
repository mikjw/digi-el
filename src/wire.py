class Wire():
    def __init__(self, branches=1):
        self.branch_count_limit = 10
        self.branch_count = 0
        self.in_connection = None
        self.in_signal = None
        self.out_connections = {}
        self.out_signal = None
        
        self.add_branch(branches)

    def connect_next(self, comp, out_terminal, in_terminal): 
        try: 
            if (out_terminal in self.out_connections):
                self.out_connections[out_terminal] = comp
                self.out_connections[out_terminal].connect_previous(self, in_terminal)
            else: 
                raise ValueError("Connection failed - invalid terminal") 
        except ValueError as err:
            print(err)
                        
    def connect_previous(self, comp):
        self.in_connection = comp

    def receive_signal(self, signal):
        self.in_signal = signal
        self.__propagate_signal(self.in_signal)
        self.__transmit_signal()
                
    def add_branch(self, number_to_add=1):
        try:
            if (self.branch_count + number_to_add <= self.branch_limit):
                for i in range(number_to_add):
                    self.branch_count += 1
                    label = chr(self.branch_count + 64)
                    self.out_connections[label] = None
            else:
                raise ValueError("Cannot add branch - limit reached") 
        except ValueError as err:
            print(err)
            
    def __propagate_signal(self, signal):
        self.out_signal = signal
            
    def __transmit_signal(self):
        for key in self.out_connections:
            if (self.out_connections[key] is not None): 
                self.out_connections[key].receive_signal(self, self.out_signal)
