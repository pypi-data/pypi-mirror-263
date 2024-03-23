from silence_tensorflow import silence_tensorflow

silence_tensorflow()
import keras as ks
import tensorflow as tf

tf.experimental.numpy.experimental_enable_numpy_behavior()

__all__ = ["Baseline", "MultiStepLastBaseline"]


class Baseline(ks.Model):
    def __init__(self, pred_col_indices: list[int], hrzn):
        super().__init__()
        self.pred_col_indices = pred_col_indices
        self.hrzn = hrzn

    def call(self, inputs):
        return inputs[:, -self.hrzn :, self.pred_col_indices]


class MultiStepLastBaseline(ks.Model):
    def __init__(self, pred_col_indices: list[int], hrzn: int):
        super().__init__()
        self.pred_col_indices = pred_col_indices
        self.hrzn = hrzn

    def call(self, inputs):
        return tf.tile(inputs[:, -1:, self.pred_col_indices], [1, self.hrzn, 1])
