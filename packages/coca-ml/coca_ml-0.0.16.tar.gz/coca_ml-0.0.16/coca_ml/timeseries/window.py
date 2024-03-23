from silence_tensorflow import silence_tensorflow

silence_tensorflow()
import keras as ks
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

__all__ = ["WindowGenerator"]


class WindowGenerator:
    def __init__(
        self,
        input_width,
        label_width,
        shift,
        train_df,
        val_df,
        test_df,
        label_columns=[],
        n_batch=32,
    ):
        self.train_df = train_df
        self.val_df = val_df
        self.test_df = test_df
        self.label_columns = label_columns if label_columns else train_df.columns
        self.n_batch = n_batch

        self.total_window_size = input_width + shift
        self.input_slice = slice(0, input_width)
        self.label_slice = slice(self.total_window_size - label_width, None)

        self.columns_indices = {name: i for i, name in enumerate(train_df.columns)}

        self.input_indices = np.arange(self.total_window_size)[self.input_slice]
        self.label_indices = np.arange(self.total_window_size)[self.label_slice]

    def plot(self, plot_col, model=None, max_subplots=3):
        plot_col_idx = self.columns_indices[plot_col]
        label_col_idx = {name: i for i, name in enumerate(self.label_columns)}.get(
            plot_col
        )

        inputs, labels = self.example
        n_plot = min(max_subplots, len(inputs))
        fig, ax = plt.subplots(nrows=n_plot, ncols=1, figsize=(12, 8))
        for i in range(n_plot):
            ax[i].set_ylabel(f"{plot_col}")
            # plot inputs
            ax[i].plot(
                self.input_indices,
                inputs[i, :, plot_col_idx],
                label="Inputs",
                marker=".",
                zorder=-10,
            )
            # plot labels
            if label_col_idx is None:
                continue
            ax[i].scatter(
                self.label_indices,
                labels[i, :, label_col_idx],
                edgecolors="k",
                label="Labels",
                c="#2ca02c",
                s=64,
            )
            # plot prediction
            if model is not None:
                predictions = model(inputs)
                ax[i].scatter(
                    self.label_indices,
                    predictions[i, :, label_col_idx],
                    marker="X",
                    edgecolors="k",
                    label="Predictions",
                    c="#ff7f0e",
                    s=64,
                )
        plt.legend(loc="best")
        plt.tight_layout()
        return fig

    def __repr__(self) -> str:
        return "\n".join(
            [
                f"Total window size: {self.total_window_size}",
                f"Input indices: {self.input_indices}",
                f"label indices: {self.label_indices}",
                f"Label column name(s): {self.label_columns}",
            ]
        )

    def split_window(self, window):
        inputs = window[:, self.input_slice, :]
        labels = tf.stack(
            [
                window[:, self.label_slice, self.columns_indices[name]]
                for name in self.label_columns
            ],
            axis=-1,
        )
        return inputs, labels

    def make_dataset(self, data):
        ds = ks.utils.timeseries_dataset_from_array(
            data=data,
            targets=None,
            sequence_length=self.total_window_size,
            sequence_stride=1,
            shuffle=True,
            batch_size=self.n_batch,
        )
        return ds.map(self.split_window)

    @property
    def train(self):
        return self.make_dataset(self.train_df)

    @property
    def val(self):
        return self.make_dataset(self.val_df)

    @property
    def test(self):
        return self.make_dataset(self.test_df)

    @property
    def example(self):
        return next(iter(self.train))
