class Wire():
    def __init__(self):
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


