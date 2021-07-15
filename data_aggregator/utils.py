import logging
import yaml
from binance.client import Client


def parse_config() -> dict:
    """Parses the config file

    Returns:
        [type]: [description]
    """
    conf_file_path = "config.yaml"
    with open(conf_file_path, 'r') as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            logging.error(exc)
    return config

def load_binance_client() -> Client:
    """ Returns the binance client """
    config = parse_config()
    api_key, api_secret = config['API_KEYS']['BINANCE']['ACCESSKEY'], config['API_KEYS']['BINANCE']['SECRETKEY']
    client = Client(api_key, api_secret)
    return client