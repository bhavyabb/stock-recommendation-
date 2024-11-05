

# Stock Analysis and Recommendation Tool

This project provides a graphical interface to analyze and compare the historical performance of stocks using data from Yahoo Finance. Built with Tkinter for GUI and `yfinance` for data retrieval, this tool displays adjusted close prices for individual stocks, compares multiple stocks, and offers recommendations based on historical performance.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [License](#license)

## Project Overview

This tool enables users to:
- View historical price trends for individual stocks.
- Compare the performance of multiple stocks over time.
- Receive basic stock recommendations based on historical maximum prices.

## Features

1. **Single Stock Analysis**: Visualizes the adjusted close price of a specified stock from 1990-01-01 to 2021-07-12.
2. **Multi-Stock Comparison**: Compares the adjusted close prices of multiple stocks on a single graph.
3. **Recommendation System**: Provides a basic recommendation by identifying stocks with the highest historical maximum prices from the selected list.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Stock-Analysis-Tool.git
   cd Stock-Analysis-Tool
   ```

2. **Install required libraries**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

## Usage

1. **Launch the application**:
   - Run the script to open the GUI.

2. **Analyze a Single Stock**:
   - Enter the stock symbol (e.g., `AAPL` for Apple).
   - Click the "Analyze" button under "Analyze a single stock" to view its adjusted close price over time.

3. **Compare Multiple Stocks**:
   - Enter multiple stock symbols separated by commas (e.g., `AAPL,GOOGL,MSFT`).
   - Click the "Analyze" button under "Compare multiple stocks" to see a comparative graph.

4. **Get Stock Recommendations**:
   - Enter multiple stock symbols separated by commas (e.g., `AAPL,GOOGL,MSFT`).
   - Click "Our expert recommendations" to view top recommended stocks based on historical maximum prices.

## Dependencies

This project requires the following Python libraries:
- `tkinter`
- `yfinance`
- `matplotlib`
- `pandas`

Install all dependencies by running:
```bash
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

