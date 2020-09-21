class Wire():
    def __init__(self):
        self.branch_count = 1
        self.in_connnection = None
        self.in_signal = None
        
        self.out_connections = {
            'A': None
        }
        
        self.out_signals = {
            'A': None
        }

    def connect_next(self, comp, terminal):
        self.out_connections['A'] = comp
        self.out_connections['A'].__connect_previous(self)

    def __connect_previous(self, comp):
        self.in_conn = comp

    def receive_signal(self, signal):
        self.in_signal = signal
        
    def add_branch(self):
        try:
            if (self.branch_count < 10):
                self.branch_count += 1
                label = chr(self.branch_count + 64)
                self.out_connections[label] = None
                self.out_signals[label] = None
            else:
                raise ValueError("Cannot add branch - limit reached"); 
        except ValueError as err:
            print(err)
  

