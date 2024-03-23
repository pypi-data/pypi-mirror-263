from silence_tensorflow import silence_tensorflow

silence_tensorflow()

import keras as ks
import pandas as pd
import tensorflow as tf

__all__ = ["ArLstm"]


class ArLstm(ks.Model):
    def __init__(self, units, out_steps, train: pd.DataFrame):
        super().__init__()
        self.out_steps = out_steps
        self.lstm_cell = ks.layers.LSTMCell(units)
        self.lstm_rnn = ks.layers.RNN(self.lstm_cell, return_state=True)
        self.dense = ks.layers.Dense(train.shape[1])

    def call(self, inputs, training=None):
        x, *state = self.lstm_rnn(inputs)
        prediction = self.dense(x)
        predictions = [prediction]
        for _ in range(1, self.out_steps):
            x = prediction
            x, state = self.lstm_cell(x, states=state, training=training)
            prediction = self.dense(x)
            predictions.append(prediction)
        predictions = tf.stack(predictions)
        predictions = tf.transpose(predictions, [1, 0, 2])
        return predictions
