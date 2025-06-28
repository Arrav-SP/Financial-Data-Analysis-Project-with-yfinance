# Financial-Data-Analysis-Project-with-yfinance
Certainly! Here’s a **clean, well-structured README** section for your project, consolidating all your features and details for clarity and professionalism:

## Features

- **Stock Lookup:** Enter any valid stock ticker (e.g., `AAPL`, `MSFT`, `TSLA`) to fetch live data.
- **Financial Dashboard:** View company info, sector, current price, market cap, latest price data, income statement, dividend history, and top institutional holders in a scrollable text tab.
- **Visual Analysis:** Instantly generate four professional charts:
  - 1-year price history (line chart)
  - 1-year trading volume (bar chart)
  - Top 5 institutional holders (bar chart)
  - Analyst recommendations (color-coded bar chart)
- **Tabbed Interface:** Clean separation between raw data and visual insights using a tabbed layout.
- **Error Handling:** User-friendly pop-ups for invalid input or data fetch issues.

## How It Works

- **GUI:** Built with `tkinter` and `ttk` for a modern, responsive interface.
- **Data Fetching:** Uses `yfinance` to retrieve real-time and historical data from Yahoo Finance.
- **Data Display:** Financial statements and summaries shown in a scrollable text widget.
- **Charts:** All plots are generated with `matplotlib` and embedded directly into the GUI.
- **Tabbed Layout:** `ttk.Notebook` keeps data and visualizations organized.

## Code Structure

- **FinancialTrackerApp class:** Handles all UI, data fetching, and chart generation.
- **display_financial_data:** Populates the text tab with company info, price data, income statement, dividends, and holders.
- **create_charts:** Produces and embeds all four visualizations in the charts tab.

## Requirements

- Python 3.7+
- yfinance
- pandas
- matplotlib
- tkinter (comes with Python)

## License

This project is open-source and free to use for learning, research, or personal finance analysis.

## Acknowledgements

- Yahoo Finance for data
- yfinance library
- matplotlib for plotting
- Python’s built-in tkinter for GUI

## Author

Developed by [Your Name]. Inspired by a hands-on, self-directed learning approach to app development and financial data analysis.

**Feel free to fork, modify, or extend this project!**
