import logging
import pandas as pd
import requests
import datetime 
import os
from typing import Union
from datetime import datetime as dt

logging.basicConfig(level=logging.INFO)

class CoinmarketcapWrapper:
    API_ADDRESS = r'https://pro-api.coinmarketcap.com'
    CMK_DAILY_HISTORY = r"https://web-api.coinmarketcap.com/v1/cryptocurrency/ohlcv/historical"
    LIMIT = 500

    def __init__(self, api_key: str, s3_bucket: str):
        self.latest = pd.DataFrame() # Filled by get_latest method
        self.api_key = api_key
        self.s3_bucket = s3_bucket

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

    def get_latest(self, debug=False) -> pd.DataFrame:
        """ This is the only call with the official API """
        url = r"https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

        # CMC_PRO_API_KEY
        params = {'CMC_PRO_API_KEY': self.api_key, 'limit': self.LIMIT}
        try:
            self.latest = pd.DataFrame(map(self.process_quote, requests.get(url, params=params).json()['data']))
        except KeyError as e:
            logging.error(params)
            raise e
        except Exception as e:
            raise e
        logging.info(f"Downloaded {self.latest.shape[0]} tokens")

        # Save output to S3
        current_time = dt.now().strftime(r"%Y%m%d%H%M")
        s3_save_path =  self.s3_bucket + "/hourly_cmk" + f"/cmk_latest_{current_time}.parquet"
        logging.info(f'Saving file to {s3_save_path}')
        if debug:
            logging.info(f"Running in DEBUG mode")
        else:
            self.latest.to_parquet(s3_save_path)
        return self.latest 

    @staticmethod
    def process_quote(input_quote: dict) -> dict:
        """Processed the CMK api latest quotes """
        base_cols_to_keep = {k: v for k, v in input_quote.items() if k != 'quote'}
        currency_quotes_cols = ('price', 'volume_24h', 'market_cap')
        for currency, quote in input_quote['quote'].items():
            quotes = {f"{currency}_{k}": v for k, v in quote.items()  if k in currency_quotes_cols}
            quotes.update({k: v for k, v in quote.items() if k not in currency_quotes_cols})

        return {**base_cols_to_keep, **quotes}

