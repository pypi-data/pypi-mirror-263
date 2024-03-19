from sz.core.model import Model
from sz.layers.linear import Linear
from sz.layers.rnn import Rnn


class SimpleRnn(Model):

    def __init__(self, hidden_size, out_size):
        super().__init__()
        self.rnn = Rnn(hidden_size)
        self.fc = Linear(out_size)

    def reset_state(self):
        self.rnn.reset_state()

    def forward(self, x):
        h = self.rnn(x)
        y = self.fc(h)
        return y
