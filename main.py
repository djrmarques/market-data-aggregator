import argparse
import logging
import os
import shutil

from numpy import dot
from data_aggregator.crypto import coinmarketcap
import dotenv

logging.basicConfig(level=logging.DEBUG)

# Find the dotenv file
env_file = dotenv.find_dotenv()
if env_file != "":
    logging.info(f"Found .env file at {env_file}")
    config = dotenv.load_dotenv(env_file)
else:
    logging.warning(f".env file not found")
    config={}

output_folder = 'output'
if not os.path.exists(output_folder):
    logging.info(f'Creating output folder at {output_folder}')
    os.makedirs(output_folder)

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-do', '--delete-output-folder', action='store_true', help='Deletes and recreates the output folder')
parser.add_argument('-di', '--debug-inputs', action='store_true', help='Prints the inputs.')
parser.add_argument('-l', '--latest-coinmarketcap', action='store_true', help='Gets the latest info from Coinmarketcap.')
parser.add_argument('-fh', '--full-history-coinmarketcap', action='store_true', help='Gets the full history from Coinmarketcap.')
args = parser.parse_args()

if args.delete_output_folder:
    logging.warning(f"Deleting the output folder and everything in it")
    shutil.register_archive_format(output_folder)
    os.makedirs(output_folder)

if args.debug_inputs:
    logging.debug(f"Input Arguments {args}")
    logging.debug(f"Config{config}")
    
if args.latest_coinmarketcap:
    cmk = coinmarketcap.CoinmarketcapWrapper(os.environ['COINMARKETCAPKEY'], os.environ['OUTPUT_S3'])
    cmk.get_latest()