import pandas as pd
import requests
from data_aggregator.utils import parse_config

config = parse_config()

class CoinmarketcapWrapper:
    API_KEY = config['COINMARKETCAP']['KEY']
    API_ADDRESS = r'https://pro-api.coinmarketcap.com'

    def __init__(self):
        self.latest = pd.DataFrame() # Filled by get_latest method

    def get_full_ticker_histtory(self):
        pass


    def get_latest(self) -> pd.DataFrame:
        """ This is the only call with the official API """
        url = self.API_ADDRESS + r'/v1/cryptocurrency/listings/latest'

        # CMC_PRO_API_KEY
        req = requests.get(url, params={'CMC_PRO_API_KEY': self.API_KEY})
        return pd.read_json(req.json()) 

