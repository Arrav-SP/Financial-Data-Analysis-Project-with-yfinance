#COMMENTS ARE CREATED USING AI

# from matplotlib.figure import Figure  # Used to create figure objects for plotting charts in matplotlib.
import tkinter as tk  # Standard Python library for creating GUI applications.
from tkinter import ttk, scrolledtext, messagebox  # ttk: themed widgets; scrolledtext: text widget with scrollbar; messagebox: popup dialogs.
import yfinance as yf  # Library to fetch financial data directly from Yahoo Finance.
import matplotlib.pyplot as plt  # Pyplot interface for matplotlib, useful for creating plots.
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Embeds matplotlib figures inside a Tkinter widget.
import pandas as pd  # Data analysis library, used here for DataFrame manipulation (yfinance returns DataFrames).

class FinancialTrackerApp:
    def __init__(self, root):
        self.root = root  # Store reference to the main Tkinter window for use throughout the class.
        self.root.title("Financial Data Tracker")  # Set the window title.
        self.root.geometry("1200x800")  # Set the window size (width x height in pixels).
        self.setup_ui()  # Call the method that builds the entire user interface.

    def setup_ui(self):
        # ----- Input Frame -----
        input_frame = ttk.Frame(self.root, padding=10)  # Create a frame for ticker input and fetch button with some padding.
        input_frame.pack(fill='x')  # Make the input frame stretch horizontally at the top of the window.

        # ----- Output Frame -----
        output_frame = ttk.Frame(self.root)  # Frame to hold the main content (tabs for data and charts).
        output_frame.pack(fill='both', expand=True, padx=10, pady=5)  # Fill all available space, with padding.

        # ----- Input Section -----
        ttk.Label(input_frame, text="Stock Ticker:").pack(side='left')  # Label for the ticker input box.
        self.ticker_entry = ttk.Entry(input_frame, width=15)  # Entry widget for user to type ticker symbol.
        self.ticker_entry.pack(side='left', padx=5)  # Place it next to the label, with a little space.
        self.ticker_entry.insert(0, "AAPL")  # Pre-fill with "AAPL" so user can try it instantly.

        fetch_btn = ttk.Button(input_frame, text="Fetch Data", command=self.fetch_data)  # Button to trigger data fetch.
        fetch_btn.pack(side='left', padx=5)  # Place it next to the entry box.

        # ----- Notebook (Tabs) -----
        self.notebook = ttk.Notebook(output_frame)  # Create a notebook (tabbed interface).
        self.notebook.pack(fill='both', expand=True)  # Fill all available space in output_frame.

        # ----- Data Tab -----
        self.data_tab = ttk.Frame(self.notebook)  # Tab for textual financial data.
        self.notebook.add(self.data_tab, text="Financial Data")  # Add the tab to the notebook.
        self.data_text = scrolledtext.ScrolledText(
            self.data_tab, wrap=tk.WORD, font=("Consolas", 9)
        )  # A scrollable text area for displaying lots of data.
        self.data_text.pack(fill='both', expand=True)  # Fill all available space in the tab.

        # ----- Charts Tab -----
        self.charts_tab = ttk.Frame(self.notebook)  # Tab for visualizations (charts).
        self.notebook.add(self.charts_tab, text="Visual Analysis")  # Add the tab to the notebook.

        # ----- Chart Grid -----
        self.chart_frame = ttk.Frame(self.charts_tab)  # Container for all charts, to be arranged in a grid.
        self.chart_frame.pack(fill='both', expand=True)  # Fill all space in the charts tab.

        # Create 2x2 grid for four charts (price, volume, holders, analyst recommendations)
        self.price_chart_frame = ttk.Frame(self.chart_frame)
        self.price_chart_frame.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)  # Top-left cell

        self.volume_chart_frame = ttk.Frame(self.chart_frame)
        self.volume_chart_frame.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)  # Top-right cell

        self.holders_chart_frame = ttk.Frame(self.chart_frame)
        self.holders_chart_frame.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)  # Bottom-left cell

        self.analyst_chart_frame = ttk.Frame(self.chart_frame)
        self.analyst_chart_frame.grid(row=1, column=1, sticky='nsew', padx=5, pady=5)  # Bottom-right cell

        # Make grid cells expand equally when window is resized
        self.chart_frame.grid_rowconfigure(0, weight=1)
        self.chart_frame.grid_rowconfigure(1, weight=1)
        self.chart_frame.grid_columnconfigure(0, weight=1)
        self.chart_frame.grid_columnconfigure(1, weight=1)

        self.ai_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.ai_tab, text="AI Analysis")
        self.ai_text = scrolledtext.ScrolledText(self.ai_tab, wrap=tk.WORD, font=("Consolas", 9))
        self.ai_text.pack(fill='both', expand=True)


    def run_ai_analysis(self):
        self.ai_text.delete('1.0', tk.END)
        stock = self.stock
        hist = stock.history(period="1y")
        if hist.empty:
            self.ai_text.insert(tk.END, "No historical data available for analysis.\n")
            return

        # Example: Trend detection and volatility analysis
        close = hist['Close']
        pct_change = close.pct_change().dropna()
        avg_return = pct_change.mean()
        volatility = pct_change.std()

        if avg_return > 0.001:
            trend = "UPWARD"
        elif avg_return < -0.001:
            trend = "DOWNWARD"
        else:
            trend = "SIDEWAYS"

        self.ai_text.insert(tk.END, f"AI Analysis for {self.ticker_entry.get().upper()}:\n\n")
        self.ai_text.insert(tk.END, f"Trend (last 1 year): {trend}\n")
        self.ai_text.insert(tk.END, f"Average Daily Return: {avg_return:.4f}\n")
        self.ai_text.insert(tk.END, f"Volatility (Std Dev): {volatility:.4f}\n")

        # Example: Simple recommendation
        if trend == "UPWARD" and avg_return > 0.002:
            self.ai_text.insert(tk.END, "\nAI Suggestion: The stock is showing a strong upward trend. Consider further analysis for potential investment.\n")
        elif trend == "DOWNWARD":
            self.ai_text.insert(tk.END, "\nAI Suggestion: The stock is in decline. Caution is advised.\n")
        else:
            self.ai_text.insert(tk.END, "\nAI Suggestion: The stock is relatively stable. Monitor for changes.\n")

    def fetch_data(self):
        # Get the ticker symbol from the entry field, remove whitespace, and convert to uppercase for consistency.
        ticker = self.ticker_entry.get().strip().upper()
        if not ticker:
            # If the user didn't enter anything, show a warning dialog.
            messagebox.showwarning("Input Error", "Please enter a stock ticker symbol.")
            return

        try:
            # Fetch the stock data using yfinance's Ticker object.
            self.stock = yf.Ticker(ticker)
            # Display the textual financial data in the data tab.
            self.display_financial_data()
            # Create and display all the charts in the charts tab.
            self.create_charts()
            self.run_ai_analysis()
        except Exception as e:
            # If anything fails (e.g., bad ticker, no internet), show an error dialog.
            messagebox.showerror("Error", f"Failed to fetch data: {str(e)}")

    def display_financial_data(self):
        self.data_text.delete('1.0', tk.END)  # Clear previous output in the text box.
        stock = self.stock  # Reference to the fetched stock object.

        # ----- Basic Company Info -----
        info = stock.info  # Get metadata dictionary from yfinance.
        self.data_text.insert(tk.END, f"Company: {info.get('longName', 'N/A')}\n")
        self.data_text.insert(tk.END, f"Sector: {info.get('sector', 'N/A')}\n")
        self.data_text.insert(tk.END, f"Current Price: ${info.get('currentPrice', 'N/A')}\n")
        self.data_text.insert(tk.END, f"Market Cap: ${info.get('marketCap', 'N/A'):,}\n\n")

        # ----- Historical Price Data -----
        hist = stock.history(period="1y")  # Get 1 year of historical prices as a DataFrame.
        if not hist.empty:
            self.data_text.insert(tk.END, "Latest Price Data:\n")
            self.data_text.insert(tk.END, hist.tail().to_string() + "\n\n")  # Show the last few rows.

        # ----- Income Statement -----
        try:
            income_stmt = stock.income_stmt  # Get income statement DataFrame.
            self.data_text.insert(tk.END, "Income Statement (Recent):\n")
            self.data_text.insert(tk.END, income_stmt.head().to_string() + "\n\n")  # Show the first few rows.
        except:
            pass  # If unavailable, skip.

        # ----- Dividend History -----
        divs = stock.dividends  # Get dividend Series (date-indexed).
        if not divs.empty:
            self.data_text.insert(tk.END, "Dividend History:\n")
            self.data_text.insert(tk.END, divs.tail().to_string() + "\n\n")  # Show the last few dividends.

        # ----- Institutional Holders -----
        holders = stock.institutional_holders  # Get institutional holders DataFrame.
        if holders is not None and not holders.empty:
            self.data_text.insert(tk.END, "Top Institutional Holders:\n")
            self.data_text.insert(tk.END, holders[['Holder', 'Shares', 'Value']].to_string() + "\n")

    def create_charts(self):
        # Remove any previous charts from the chart frames to avoid overlap or memory leaks.
        for widget in self.price_chart_frame.winfo_children():
            widget.destroy()
        for widget in self.volume_chart_frame.winfo_children():
            widget.destroy()
        for widget in self.holders_chart_frame.winfo_children():
            widget.destroy()
        for widget in self.analyst_chart_frame.winfo_children():
            widget.destroy()

        # Create and display each chart in its respective frame.
        self.create_price_chart()
        self.create_volume_chart()
        self.create_holders_chart()
        self.create_analyst_chart()

    def create_price_chart(self):
        hist = self.stock.history(period="1y")  # Get 1 year historical data as a DataFrame.
        if hist.empty:
            return  # Do nothing if no data is available.

        # Create a matplotlib Figure for the price chart.
        fig = Figure(figsize=(5, 3), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot(hist.index, hist['Close'], label='Closing Price', color='blue')  # Plot closing prices.
        ax.set_title('Price History (1 Year)')
        ax.set_ylabel('Price ($)')
        ax.grid(True)
        ax.legend()

        # Embed the chart in the Tkinter frame using FigureCanvasTkAgg.
        canvas = FigureCanvasTkAgg(fig, master=self.price_chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)

    def create_volume_chart(self):
        hist = self.stock.history(period="1y")  # Get 1 year historical data as a DataFrame.
        if hist.empty:
            return  # Do nothing if no data is available.

        # Create a matplotlib Figure for the volume chart.
        fig = Figure(figsize=(5, 3), dpi=100)
        ax = fig.add_subplot(111)
        ax.bar(hist.index, hist['Volume'], color='green', alpha=0.7)  # Bar chart for trading volume.
        ax.set_title('Trading Volume')
        ax.set_ylabel('Volume')
        ax.grid(True)

        # Embed the chart in the Tkinter frame.
        canvas = FigureCanvasTkAgg(fig, master=self.volume_chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)

    def create_holders_chart(self):
        holders = self.stock.institutional_holders  # Get institutional holders DataFrame.
        if holders is None or holders.empty:
            return  # Do nothing if no data is available.

        # Prepare top 5 holders and calculate their percent ownership.
        top_holders = holders.head(5).copy()
        top_holders['Pct Ownership'] = (top_holders['Shares'] / top_holders['Shares'].sum()) * 100

        # Create a matplotlib Figure for the holders chart.
        fig = Figure(figsize=(5, 3), dpi=100)
        ax = fig.add_subplot(111)
        top_holders.plot.bar(x='Holder', y='Pct Ownership', ax=ax, color='purple')
        ax.set_title('Top Institutional Holders')
        ax.set_ylabel('% of Total Holdings')
        ax.tick_params(axis='x', rotation=15)  # Rotate x labels for readability.
        ax.grid(True)

        # Embed the chart in the Tkinter frame.
        canvas = FigureCanvasTkAgg(fig, master=self.holders_chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)

    def create_analyst_chart(self):
        try:
            rec = self.stock.recommendations  # Get analyst recommendations DataFrame.
            if rec is None or rec.empty:
                return  # Do nothing if no data is available.

            # Get the latest row of recommendation summary.
            latest = rec.iloc[-1]
            categories = ['strongBuy', 'buy', 'hold', 'sell', 'strongSell']
            counts = [latest[c] for c in categories]

            # Create a matplotlib Figure for the analyst recommendations chart.
            fig = Figure(figsize=(5, 3), dpi=100)
            ax = fig.add_subplot(111)
            ax.bar(categories, counts, color=['green', 'lightgreen', 'yellow', 'orange', 'red'])
            ax.set_title('Analyst Recommendations')
            ax.set_ylabel('Number of Analysts')
            ax.grid(True)

            # Embed the chart in the Tkinter frame.
            canvas = FigureCanvasTkAgg(fig, master=self.analyst_chart_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill='both', expand=True)
        except:
            pass  # If any error occurs, skip this chart.

# Main entry point for the application.
if __name__ == "__main__":
    root = tk.Tk()  # Create main Tkinter window.
    app = FinancialTrackerApp(root)  # Instantiate the app class with the window.
    root.mainloop()  # Start the Tkinter event loop (keeps the window open and responsive).
