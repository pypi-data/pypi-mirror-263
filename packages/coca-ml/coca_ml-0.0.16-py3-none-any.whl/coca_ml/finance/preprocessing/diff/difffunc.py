import numpy as np
import pandas as pd
from numba import njit

__all__ = ["transform"]


def transform(X: pd.DataFrame, d: float, thresh=0.01):
    w = get_weights(d, X.shape[0])
    skip = get_skip(w, thresh)

    data = X.values
    out = np.zeros(data.shape, dtype=np.float64)
    for i_col in range(data.shape[1]):
        target = X.iloc[:, i_col].ffill().dropna().values.astype(np.float64)
        diff(skip, target, data, out, i_col, w)
    df = pd.DataFrame(out, index=X.index, columns=X.columns)
    return df[df[X.columns] != 0].dropna()


@njit
def diff(skip, target, data, out, i_col, w):
    for i_row in range(skip, target.shape[0]):
        if not np.isfinite(data[i_row, i_col]):
            continue
        out[i_row, i_col] = np.dot(w[-(i_row + 1) :].T, target[: i_row + 1])[0]


@njit
def get_weights(d, size):
    w = [1.0]
    for k in range(1, size):
        w_ = -w[-1] / k * (d - k + 1)
        w.append(w_)
    w = np.array(w[::-1]).reshape(-1, 1)
    return w


@njit
def get_skip(w, thresh):
    w_ = np.cumsum(np.abs(w))
    w_ /= w_[-1]
    skip = w_[w_ > thresh].shape[0]
    return skip
