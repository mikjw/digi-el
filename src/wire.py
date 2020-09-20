class Wire():
    def __init__(self):
        self.branch_count = 1
        self.in_conn = None
        self.out_conn_a = None
        self.in_signal = None
        self.out_signal_a = None

    def connect_next(self, comp):
        self.out_conn_a = comp
        self.out_conn_a.__connect_previous(self)

    def __connect_previous(self, comp):
        self.in_conn = comp

    def receive_signal(self, signal):
        self.in_signal = signal
        
    def add_branch(self):
        try:
            if (self.branch_count < 10):
                self.branch_count += 1
                label = chr(self.branch_count + 96)
                new_attr_conn = f'out_conn_{label}'
                new_attr_signal = f'out_signal_{label}'
                setattr(self, new_attr_conn, None)
                setattr(self, new_attr_signal, None)
            else:
                raise ValueError("Cannot add branch - limit reached"); 
        except ValueError as err:
            print(err)

