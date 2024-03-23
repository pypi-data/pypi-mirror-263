import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

__all__ = ["BalanceOfPower"]


class BalanceOfPower(BaseEstimator, TransformerMixin):
    def fit(self, X: pd.DataFrame):
        return self

    def transform(self, X: pd.DataFrame):
        X["BOP"] = (X.close - X.open) / (X.high - X.low)
        return X
