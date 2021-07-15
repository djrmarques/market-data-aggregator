from typing import List
from data_aggregator.utils import load_binance_client
import pandas as pd

class BinanceWrapper():
    """ This class will act as a wrapper for the Binance API, that will download all the necessary information for the tool """
    def __init__(self):
        pass

    def get_top_tickers_by_mc(n=100) -> List[str]:
        """Imports the top tickers by aggregator    

        Args:
            n (int, optional): Number of Tickers to download. Defaults to 100.

        Returns:
            List[str]: List of ticker symbols to download
        """
        raise NotImplementedError

    def download_usd_price(self, ticker: str) -> pd.Series:
        """Downloads the price for each ticker
        """
        raise NotImplementedError

    def download_and_save_to_s3(self) -> None:
        """ Downloads everything and saves it to the designated S3 bucket"""
        raise NotImplementedError