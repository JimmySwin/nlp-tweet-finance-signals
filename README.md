📄 Design Doc Outline (Phase 0 Deliverable)
Title: Modeling Market Reaction to High-Impact Tweets
Author: James
Date: [TBD]

1. Objective
This project aims to use NLP and time series to predict the affect that influential people have on the price of
various stocks after simple tweets.

2. Hypotheses
Tweets contain predictive signal.

Sentiment/keywords correlate with market direction/volatility.

Market reacts differently depending on instrument (SPY vs BTC).

3. Scope & Constraints
Assets: [e.g., TSLA, BTC]

Tweet source: [e.g., Kaggle Musk dataset, date range]

Market data: [e.g., yfinance 1-min bars]

Time horizon: [e.g., return over 5m, 30m]

Type of prediction: [classification of return sign, regression of return magnitude, vol spike detection]

4. Evaluation Plan
Metrics for classification/regression.

Time-based validation strategy (split, purged K-Fold, embargo).

Leakage cautions.

5. Baseline Models
NLP: [e.g., VADER/FinBERT sentiment scores, tweet metadata]

Models: [e.g., logistic regression for direction]

6. Reproducibility Plan
Folder structure.

Logging tools (e.g., experiment.csv + MLflow optional).

Environment management (requirements.txt).

7. Future Enhancements
BERT embeddings.

Aggregated multi-tweet clusters.

Backtesting simulated trading strategy.