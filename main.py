import argparse
import logging
import os
import shutil
from data_aggregator.crypto import coinmarketcap
from data_aggregator.utils import parse_config

output_folder = 'output'
if not os.path.exists(output_folder):
    logging.info(f'Creating output folder at {output_folder}')
    os.makedirs(output_folder)

logging.basicConfig(level=logging.DEBUG)

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-do', '--delete-output-folder', action='store_true', help='Deletes and recreates the output folder')
parser.add_argument('-di', '--debug-inputs', action='store_true', help='Prints the inputs.')
parser.add_argument('-l', '--latest-coinmarketcap', action='store_true', help='Gets the latest info from Coinmarketcap.')
parser.add_argument('-fh', '--full-history-coinmarketcap', action='store_true', help='Gets the full history from Coinmarketcap.')
parser.add_argument('-s', '--save-s3', action='store_true', help='Save the results into the appropriate S3 bucket')

args = parser.parse_args()

if args.delete_output_folder:
    logging.warning(f"Deleting the output folder and everything in it")
    shutil.register_archive_format(output_folder)
    os.makedirs(output_folder)

if args.debug_inputs:
    config = parse_config()
    logging.debug(f"{args}")
    logging.debug(f"{config}")
    
if args.latest_coinmarketcap:
    cmk = coinmarketcap.CoinmarketcapWrapper()
    latest_df = cmk.get_latest()




