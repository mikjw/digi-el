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
        lowercase_label = chr(ord(terminal) + 32)
        setattr(self, f'in_connection_{lowercase_label}', comp)

        