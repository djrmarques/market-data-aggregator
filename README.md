[![Test Build](https://github.com/djrmarques/market-data-aggregator/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/djrmarques/market-data-aggregator/actions/workflows/test.yml)

# market-data-aggregator
Tool to gather and store market data from various places into a private S3 bucket.

# Setup
1. Get a Coinmarketcap API key

Follow https://coinmarketcap.com/api/

2. Create a *.env* file with the following credentials 

```sh
# S3 bucket output
OUTPUT_S3='s3-bucket'

# Coinmarketcap API
COINMARKETCAPKEY='cmk-api-key'
```

3. Setup AWS credentials

Follow https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html. Requires AWS account.

# Running

## Saving the lastest data using CoinMarketCap
```sh
pip install -r requirements.txt
python main.py -l
```
