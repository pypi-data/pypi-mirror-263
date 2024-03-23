import numpy as np
import pandas as pd
from numba import njit

__all__ = ["transform"]


def transform(X: pd.DataFrame, d: float, thresh=1e-5):
    w = get_weights(d, thresh)

    data = X.values
    out = np.zeros(data.shape, dtype=np.float64)
    for i_col in range(data.shape[1]):
        target = X.iloc[:, i_col].ffill().dropna().values.astype(np.float64)
        diff(target, data, out, i_col, w)
    df = pd.DataFrame(out, index=X.index, columns=X.columns)
    return df[df[X.columns] != 0].dropna()


@njit
def get_weights(d, thres):
    w, k = [1.0], 1
    while True:
        w_ = -w[-1] / k * (d - k + 1)
        if abs(w_) < thres:
            break
        w.append(w_)
        k += 1
    return np.array(w[::-1]).reshape(-1, 1)


@njit
def diff(target, data, out, i_col, w):
    width = len(w) - 1
    for i_row in range(width, target.shape[0]):
        i_loc0, i_loc1 = i_row - width, i_row
        if not np.isfinite(data[i_row, i_col]):
            continue
        out[i_row, i_col] = np.dot(w.T, target[i_loc0 : i_loc1 + 1])[0]
