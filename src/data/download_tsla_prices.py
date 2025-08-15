# File: src/data/download_tsla_prices.py

import yfinance as yf
import pandas as pd

# Download daily TSLA OHLCV data (2022–2023 to match your Musk tweets)
df = yf.download("TSLA", start="2022-07-01", end="2023-07-01", interval="1d")

# Check a preview
print(df.head())

# Save to the raw data folder
output_path = "/home/james/finance_job/NLP_market_reaction/data/raw/tsla_ohlcv_daily.csv"
df.to_csv(output_path)
print(f"Saved to: {output_path}")
