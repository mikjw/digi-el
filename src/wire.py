class Wire():
    def __init__(self):
        self.in_conn = None
        self.out_conn = None

    def connect_next(self, component):
        self.out_conn = component
