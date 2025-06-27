# Import necessary libraries
import yfinance as yf  # Official Yahoo Finance API wrapper for Python

"""
WHY WE USE YFINANCE:
- Avoids complex web scraping and HTML parsing
- Provides structured financial data in pandas DataFrames
- Handles API rate limits and data normalization automatically
"""

# Create a Ticker object for Apple Inc. (AAPL)
aapl = yf.Ticker("AAPL")
"""
WHY WE CREATE A TICKER OBJECT:
- This is the primary interface for accessing all financial data
- The ticker symbol ("AAPL") can be replaced with any valid stock symbol
- The object contains methods to access 20+ data categories
"""

# 1. HISTORICAL PRICE DATA EXTRACTION
hist_data = aapl.history(period="1y")
"""
WHY HISTORICAL DATA:
- Essential for technical analysis and price trend visualization
- 'period' parameter controls date range (options: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max)
- Returns OHLC (Open-High-Low-Close) prices plus volume and dividends
"""

# 2. INCOME STATEMENT ANALYSIS
income_stmt = aapl.income_stmt
print(income_stmt.loc[['Total Revenue', 'Net Income']])
"""
WHY INCOME STATEMENT:
- Shows company profitability over time
- 'Total Revenue' indicates sales performance
- 'Net Income' reveals bottom-line profitability
- Data is returned as multi-period DataFrame
"""

# 3. BALANCE SHEET SNAPSHOT
balance_sheet = aapl.balance_sheet
print(balance_sheet.loc[['Total Assets', 'Total Liabilities Net Minority Interest']])
"""
WHY BALANCE SHEET:
- Displays company's financial position at specific dates
- 'Total Assets' shows resource base
- 'Total Liabilities' indicates obligations
- Helps calculate financial health ratios
"""

# 4. CASH FLOW ANALYSIS
cash_flow = aapl.cashflow
print(cash_flow.loc[['Free Cash Flow']])
"""
WHY CASH FLOW:
- Reveals actual cash generation ability
- 'Free Cash Flow' = Operating Cash Flow - Capital Expenditures
- Key metric for dividend sustainability and investment capacity
"""

# 5. DIVIDEND HISTORY
dividends = aapl.dividends
print(f"Last 5 dividends:\n{dividends.tail()}")
"""
WHY DIVIDEND DATA:
- Critical for income investors
- Shows dividend payment history and consistency
- Helps calculate dividend yield and growth rate
"""

# 6. ANALYST RECOMMENDATIONS (UPDATED FORMAT)
recommendations = aapl.recommendations
if not recommendations.empty:
    print("\nAnalyst Recommendations Summary:")
    print(recommendations.tail())
else:
    print("\nNo analyst recommendations data available")
"""
WHY ANALYST DATA:
- Reveals market sentiment and professional outlook
- Shows aggregated analyst ratings by period
- Helps identify rating trends and consensus
"""

# 7. OPTIONS MARKET ANALYSIS
options = aapl.option_chain()
print("\nCall options:")
print(options.calls[['strike', 'lastPrice']].head())
print("\nPut options:")
print(options.puts[['strike', 'lastPrice']].head())
"""
WHY OPTIONS DATA:
- Shows market expectations for price volatility
- Call options indicate bullish sentiment
- Put options reveal bearish expectations
- Strike prices show key support/resistance levels
"""

# 8. INSTITUTIONAL OWNERSHIP
holders = aapl.institutional_holders
print("\nTop institutional holders:")
print(holders[['Holder', 'Shares', 'Value']])
"""
WHY OWNERSHIP DATA:
- Reveals "smart money" positions
- High institutional ownership typically indicates confidence
- Sudden changes may signal upcoming price movements
"""

# EXPORTING DATA (EXAMPLE)
hist_data.to_csv('aapl_historical.csv')
"""
WHY EXPORT:
- Enables further analysis in Excel, Tableau, or other tools
- Allows historical backtesting of trading strategies
- Facilitates long-term performance tracking
"""

"""
KEY LIBRARY FEATURES USED:
- yf.Ticker(): Main interface for stock data
- .history(): Historical market data
- .income_stmt/.balance_sheet/.cashflow: Financial statements
- .dividends: Dividend history
- .recommendations: Analyst ratings
- .option_chain(): Options market data
- .institutional_holders: Ownership data

ADVANCED USAGE TIPS:
1. Multiple tickers: yf.Tickers(["AAPL", "MSFT", "GOOG"])
2. Custom date range: history(start="2020-01-01", end="2023-01-01")
3. Intraday data: interval="1m" (for 1-minute data)
4. Actions parameter: history(..., actions="split") to get stock splits
5. Fast access: aapl.fast_info for quick price and volume

WHY THIS STRUCTURE WORKS:
1. Modular: Each section focuses on specific data type
2. Extensible: Easy to add more metrics (e.g., add 'EPS' to income statement)
3. Practical: Extracts most-used financial metrics by investors
4. Efficient: Minimal code for maximum data coverage
"""
