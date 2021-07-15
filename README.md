# market-data-aggregator
Tool to gather and store market data from various places into a private S3 bucket

# Settup

1. Install requirements 
```sh
pip install -r requirements.txt
```
2. Create a *project.yaml* file with the following credentials 

```yaml
OUTPUT_S3: Bucket to save the results

# Binance will be used to obtain market data
BINANCE: 
  SECRETKEY: Binance Secret
  ACCESSKEY: Binance Access Key
```