import argparse
import logging
from data_aggregator.crypto.binance import get_data_binance
from data_aggregator.utils import parse_config

logging.basicConfig(level=logging.DEBUG)

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-bt', '--binance_all-tickers', action='store_true', help='Downloads current prices from all Tickers from Binance')
parser.add_argument('-dy', '--debug-yaml', action='store_true', help='Prints the contens of the Yaml file for debug')

args = parser.parse_args()

if args.debug_yaml:
    config = parse_config()
    logging.debug(f"{config}")


if args.binance_all_tickers:
    with get_data_binance.BinanceWrapper() as client:
        print(client.get_all_tickers())



