import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

__all__ = ["Vwap"]


class Vwap(BaseEstimator, TransformerMixin):
    def fit(self, X: pd.DataFrame):
        return self

    def transform(self, X: pd.DataFrame):
        X["TP"] = (X.high + X.low + X.close) / 3
        X["VWAP"] = (X.volume * X.TP).cumsum() / X.volume.cumsum()
        return X.drop(columns="TP")
