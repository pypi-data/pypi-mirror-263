import numpy as np

from sz.core.config import Config
from sz.ds.queue import PriorityQueue


class Tensor:
    """
    张量（Tensor）是一个多维数组，它是标量、向量、矩阵的高维扩展，是一个数据容器，张量是矩阵向任意维度的推广
    """

    def __init__(self, data, name=None):
        self.data = data  # 正向传播时的变量值
        self.grad = None  # 反向传播时的导数值
        self.creator = None  # 与变量关联的函数，即f(x)与x关联的函数f
        self.generation = 0  # 表示函数属于哪一代，主要用于反向传播时确定复杂计算图的计算顺序
        self.name = name  # 张量名称

    def backward(self):
        """
        反向传播的主要目的是为了更新梯度
        """
        if Config.ENABLE_BACKPROP:
            if self.grad is None:
                self.grad = Tensor(np.ones_like(self.data))
            # ---------- 核心处理 start ----------
            priorityQueue = PriorityQueue()  # 优先队列
            priorityQueue.push(self.creator, self.generation)
            while priorityQueue.len() != 0:
                pop_creator = priorityQueue.pop()  # 获取与变量关联的函数，generation的数值越高将越优先被出队列
                xs, ys = pop_creator.inputs, pop_creator.outputs  # 获取函数的输入和输出
                gys = [y().grad for y in ys]  # 弱引用获取函数输出的导数
                """
                之所以增加判断，是因为，执行：
                for y in ys:
                    y().grad = None
                遇到类似：
                x = Tensor(np.array([2]))
                y = (x**3+x)*5
                当满足x在表达式出现多次且求高阶导数时会发生异常：
                TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
                """
                if not any([i is None for i in gys]):
                    gxs = pop_creator.backward(*gys)  # 反向传播
                    if not isinstance(gxs, tuple):
                        gxs = (gxs,)
                    for x, gx in zip(xs, gxs):
                        if x.grad is None:
                            x.grad = gx
                        else:
                            """
                            这里不能写为x.grad += gx，+=是覆盖，要用复制的写法
                            说白了就是所在内存位置的变化：类似x+=y或x[:]=x+y都是覆盖，即内存位置没变；而x=x+y是复制的写法，内存位置会变
                            """
                            x.grad = x.grad + gx
                        if x.creator is not None:
                            priorityQueue.push(x.creator, x.generation)
                    for y in ys:
                        y().grad = None
            # ---------- 核心处理 end ----------

    def clear_tensor(self):
        self.grad = None
        self.creator = None
        self.generation = 0

    def unchain(self):
        self.creator = None

    def unchain_backward(self):
        if self.creator is not None:
            funcs = [self.creator]
            while funcs:
                f = funcs.pop()
                for x in f.inputs:
                    if x.creator is not None:
                        funcs.append(x.creator)
                        x.unchain()

    def __len__(self):
        return len(self.data)

    def __repr__(self) -> str:
        return 'Tensor(None)' if self.data is None else 'Tensor(' + str(self.data) + ')'

    @property
    def shape(self):
        """ 数据的形态，如一个3行4列的二维矩阵，它的形态是：(3, 4) """
        return self.data.shape

    @property
    def size(self):
        """
        矩阵总元素个数，如A=(3,2,4)，则size=3*2*4=24
        """
        return self.data.size

    @property
    def ndim(self):
        """
        维度，如(3,8,5)，则维度为3
        """
        return self.data.ndim

    @property
    def dtype(self):
        """
        数据类型，如np.random.randn(3, 2, 1)的数据类型为：float64
        """
        return self.data.dtype

    @property
    def T(self):
        from sz.functions.ft0 import transpose
        return transpose(self)

    def transpose(self, axes=None):
        from sz.functions.ft0 import transpose
        return transpose(self, axes)

    def reshape(self, shape):
        from sz.functions.ft0 import reshape
        # 当其非元祖传入时，即x.reshape(12, 1, 2)时的处理
        if not isinstance(shape, tuple):
            shape = (shape,)
        return reshape(self, shape)


class Parameter(Tensor):
    """
    Parameter参数类与Tensor拥有相同的能力，只是对象名称不一样
    """
    pass
