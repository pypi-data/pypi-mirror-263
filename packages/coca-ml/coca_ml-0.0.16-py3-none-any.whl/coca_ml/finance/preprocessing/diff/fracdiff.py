import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

from coca_ml.finance.preprocessing.diff import difffunc, difffunc_ffd

__all__ = ["FracDiff"]


class FracDiff(BaseEstimator, TransformerMixin):
    def __init__(self, d: float, thresh=1e-5, is_ffd=True):
        super().__init__()
        self.d = d
        self.thresh = thresh
        self.is_ffd = is_ffd

    def fit(self, X: pd.DataFrame):
        return self

    def transform(self, X: pd.DataFrame):
        return (
            difffunc_ffd.transform(X, self.d, self.thresh)
            if self.is_ffd
            else difffunc.transform(X, self.d, self.thresh)
        )
