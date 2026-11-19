import yfinance as yf
import pandas as pd
import streamlit as st   # add at top with other imports, the rest at the bottom
import numpy as np
from datetime import date

def fetch_data(tickers, start_date, end_date):
    data_frames = []
    for ticker in tickers:
        stock_data = yf.download(ticker, start=start_date, end=end_date)['Close']
        data_frames.append(stock_data)
    
    data = pd.concat(data_frames, axis=1, keys=tickers)
    data.columns = tickers
    return data

def calculate_sharpe_ratio(returns, risk_free_rate=0.02):
    portfolio_return = returns.mean().mean()
    portfolio_volatility = returns.std().mean()
    return (portfolio_return - risk_free_rate) / portfolio_volatility

def calculate_sortino_ratio(returns, risk_free_rate=0.02):
    portfolio_return = returns.mean().mean()
    downside_returns = returns[returns < 0]
    downside_deviation = downside_returns.std().mean()
    return (portfolio_return - risk_free_rate) / downside_deviation

# not really optimized but better than it was!  does portfolio based on returns
def portfolio_optimization(returns):
    avg_returns = returns.mean().clip(lower=0)
    return avg_returns / avg_returns.sum()

st.title("Financial Analysis Web App")

# User inputs
tickers = st.text_input("Enter stock tickers (comma separated)", "AAPL, MSFT, GOOG").split(",")
tickers = [ticker.strip() for ticker in tickers]
start_date = st.date_input("Start Date", pd.to_datetime("2020-01-01"))
end_date = st.date_input("End Date", date.today())

# Fetch stock data
stock_data = fetch_data(tickers, start_date, end_date)
returns_data = stock_data.pct_change().dropna()

# Visualizations
st.subheader("Stock Prices")
st.line_chart(stock_data)

st.subheader("Total Return Over Time")
cumulative_returns = (1 + returns_data).cumprod() - 1
st.line_chart(cumulative_returns * 100)

sharpe_ratio = calculate_sharpe_ratio(returns_data)
sortino_ratio = calculate_sortino_ratio(returns_data)

st.subheader("Performance Metrics")
st.write(f"Sharpe Ratio: {sharpe_ratio:.2f}")
st.write(f"Sortino Ratio: {sortino_ratio:.2f}")

optimal_weights = portfolio_optimization(returns_data)

st.subheader("Portfolio Optimization")
st.write("Optimal Portfolio Weights:")
for ticker, weight in zip(tickers, optimal_weights):
    st.write(f"{ticker}: {weight:.2%}")

csv_data = stock_data.to_csv()
st.download_button("Download Stock Data CSV", csv_data, "stock_data.csv")
