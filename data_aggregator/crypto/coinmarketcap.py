import logging
import pandas as pd
import requests
import datetime 
from typing import Union
import os
from datetime import datetime as dt

logging.basicConfig(level=logging.INFO)

class CoinmarketcapWrapper:
    API_ADDRESS = r'https://pro-api.coinmarketcap.com'
    CMK_DAILY_HISTORY = r"https://web-api.coinmarketcap.com/v1/cryptocurrency/ohlcv/historical"
    LIMIT = 500

    def __init__(self, api_key: str, s3_bucket: str):
        self.latest = pd.DataFrame() # Filled by get_latest method
        self.s3_bucket = api_key
        self.api_key = s3_bucket

    def download_and_save_all_tickers(self, slug: str, start_date: Union[dt, None], end_date: Union[dt, None]) -> pd.DataFrame:
        """ Go through the list of all the tickers, downloads the daily price and saves them to S3."""

        start_date_timestamp = int(start_date.replace(tzinfo=datetime.timezone.utc).timestamp())
        end_date_timestamp = int(end_date.replace(tzinfo=datetime.timezone.utc).timestamp())
        
        params = {'convert': 'USD', 'time_end': end_date_timestamp, 'time_start': start_date_timestamp}
        req = pd.DataFrame(requests.get(self.CMK_DAILY_HISTORY, params=params).json()['data'])

    @staticmethod
    def sleep_time() -> float:
        """Number os seconds to sleep between requests

        Returns:
            float: Number os seconds to sleep between requests
        """
        raise NotImplementedError

    def get_latest(self) -> pd.DataFrame:
        """ This is the only call with the official API """
        url = self.API_ADDRESS + r'/v1/cryptocurrency/listings/latest'

        # CMC_PRO_API_KEY
        params = {'CMC_PRO_API_KEY': self.api_key, 'limit': self.LIMIT}
        self.latest = pd.DataFrame(requests.get(url, params=params).json()['data'])
        logging.info(f"Downloaded {self.latest.shape[0]} tokens with more than {self.MARKETCAP_LIMIT} Market Cap")

        # Save output to S3
        current_time = dt.now().strftime(r"%Y%m%d%H%M")
        s3_save_path =  self.s3_bucket + "/hourly_cmk" + f"/cmk_latest_{current_time}.parquet"
        self.info(f'Saving file to {s3_save_path}')
        self.latest.to_parquet(s3_save_path)
        return self.latest 

