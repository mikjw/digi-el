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
        
    def connect_previous(self, comp, terminal):
        if terminal == 'A':
            self.in_connection_a = comp
        else:
            self.in_connection_b = comp
        
        