import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

__all__ = ["DollarBar"]


class DollarBar(BaseEstimator, TransformerMixin):
    def __init__(self, col_value: str, col_volume: str, thresh=100):
        super().__init__()
        self.col_value = col_value
        self.col_volume = col_volume
        self.thresh = thresh

    def fit(self, X: pd.DataFrame):
        return self

    def transform(self, X: pd.DataFrame):
        targets = [self.col_value, self.col_volume]
        if not set(targets) <= set(X.columns):
            raise ValueError(
                f"not existed columns: {list(set(targets) - set(X.columns))}"
            )
        if not pd.api.types.is_datetime64_any_dtype(X.index):
            raise TypeError("type of index is not datetime64")

        X = X.sort_index()
        X["group"] = (X[self.col_value] * X[self.col_volume]).cumsum() // self.thresh
        grouped_df = X[[self.col_value, self.col_volume, "group"]].groupby("group")
        return (
            grouped_df[[self.col_value, self.col_volume]]
            .apply(
                lambda df: pd.Series(
                    {
                        "timestamp": df.index[-1],
                        "Open": df[self.col_value].iloc[0],
                        "High": df[self.col_value].max(),
                        "Low": df[self.col_value].min(),
                        "Close": df[self.col_value].iloc[-1],
                        "Volume": df[self.col_volume].sum(),
                    }
                )
            )
            .set_index("timestamp")
        )
