[![Test Build](https://github.com/djrmarques/market-data-aggregator/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/djrmarques/market-data-aggregator/actions/workflows/test.yml)

# market-data-aggregator
Tool to gather and store market data from various places into a private S3 bucket.

# Settup

1. Install requirements 
```sh
pip install -r requirements.txt
```
2. Create a *.env* file with the following credentials 

```sh
# S3 bucket output
OUTPUT_S3='s3-bucket'

# Coinmarketcap API
COINMARKETCAPKEY='cmk-api-key'
```

3. Setup AWS credentials