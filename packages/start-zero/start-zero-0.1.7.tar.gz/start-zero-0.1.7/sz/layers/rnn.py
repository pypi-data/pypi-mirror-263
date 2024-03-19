from sz.core.layer import Layer
from sz.layers.linear import Linear
from sz.functions.ft2 import tanh


class Rnn(Layer):

    def __init__(self, hidden_size, in_size=None):
        super().__init__()
        self.x2h = Linear(hidden_size, in_size=in_size)
        self.h2h = Linear(hidden_size, in_size=in_size, nobias=True)
        self.h = None

    def reset_state(self):
        self.h = None

    def forward(self, x):
        if self.h is None:
            h_new = tanh(self.x2h(x))
        else:
            h_new = tanh(self.x2h(x) + self.h2h(self.h))
        self.h = h_new
        return h_new
