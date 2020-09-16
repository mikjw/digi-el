class Wire():
    def __init__(self):
        self.in_conn = None
        self.out_conn = None
        self.in_signal = None
        self.out_signal = None

    def connect_next(self, comp):
        self.out_conn = comp
        self.out_conn.__connect_previous(self)

    def __connect_previous(self, comp):
        self.in_conn = comp
