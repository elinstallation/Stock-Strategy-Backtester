
# Stock Strategy Backtester

A Python tool that backtests two trading strategies — SMA Crossover and Mean Reversion (Bollinger Bands) — against a Buy and Hold benchmark across S&P 500 stocks, with an interactive Plotly dashboard to visualise the results.

---
## Demo 
https://github.com/user-attachments/assets/0ff765f0-6bfc-4fe9-8ccc-97448759b295


## Strategies

**SMA Crossover** — generates a buy signal when the 5-day moving average crosses above the 20-day moving average, and a sell signal when it crosses below.

**Mean Reversion (Bollinger Bands)** — generates a buy signal when price drops below the lower band (2 standard deviations below the 20-day SMA) and a sell signal when price rises above the upper band.

---

## Project Structure

```
├── main.py                 # Computes indicators, signals, and cumulative returns
├── app.py                  # Interactive Plotly dashboard
├── all_stocks_5yr.csv      # Input data (not included, see below)
└── backtest_results.csv    # Output from main.py (auto-generated)
```

---

## Setup

1. Clone the repo:
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. Install dependencies:
```bash
pip install pandas numpy plotly
```

3. Add your data — place `all_stocks_5yr.csv` in the root directory. The file should have these columns:
```
date, open, high, low, close, volume, Name
```
You can download a copy from [Kaggle](https://www.kaggle.com/datasets/camnugent/sandp500).

---

## Usage

First run `main.py` to generate the backtest results:
```bash
python main.py
```

Then launch the dashboard:
```bash
python app.py
```

A browser window will open with an interactive chart. Use the dropdown in the top left to switch between tickers and compare how each strategy performed against Buy and Hold.

---

## Output

The dashboard plots three cumulative return curves per ticker:

- **Buy and Hold** — passive benchmark
- **SMA returns** — SMA crossover strategy
- **Bollinger Bands returns** — mean reversion strategy

All returns are normalised to start at $1.00.
