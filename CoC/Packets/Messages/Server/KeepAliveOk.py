from Utils.Writer import Writer


class KeepAliveOk(Writer):

    def __init__(self, device):
        super().__init__(device)
        self.id = 20108
        self.device = device

    def encode(self):
        pass