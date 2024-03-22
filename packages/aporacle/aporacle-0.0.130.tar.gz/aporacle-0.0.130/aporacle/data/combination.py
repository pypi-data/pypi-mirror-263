import logging
from typing import List, Optional

import pandas as pd
from komoutils.core import KomoBase

from aporacle.data.asset import AssetData
from aporacle.data.gcp import download_csv_from_gcp_return_df
from aporacle.data.symbols import SymbolData


class Combination(KomoBase):
    def __init__(self, feed: str, symbols: List[str] = None):
        self.feed: str = feed
        self.symbols: Optional[list] = symbols
        self.combined: Optional[pd.DataFrame] = None

    def combine(self, data: List[pd.DataFrame]):
        self.combined = pd.concat(data, axis=1)
        return self.combined

    def get_from_gcp(self):
        try:
            assert len(self.symbols) > 0, f"Please provide valid symbols. "
            data: List[pd.DataFrame] = [download_csv_from_gcp_return_df(bucket_name=self.feed, symbol=symbol)
                                        for symbol in self.symbols]
            return self.combine(data)
        except AssertionError as ae:
            self.log_with_clock(log_level=logging.ERROR, msg=f"{ae}")
        except Exception as e:
            raise

    def get_from_provided(self, dfs: List[pd.DataFrame]):
        try:
            data: List[pd.DataFrame] = [df for df in dfs]
            return self.combine(data)
        except Exception as e:
            raise