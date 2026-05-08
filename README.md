Binance Futures Trading Bot (Testnet)
A robust, modular Python application designed to place orders on the Binance Futures Testnet (USDT-M). This project was developed as part of a technical assessment task for the Python Developer Internship at Primetrade.ai.

Features
Market Orders: Execute instant BUY/SELL orders at current market prices.

Limit Orders: Place BUY/SELL orders at a specific target price.

Input Validation: Robust checking for symbols, sides, quantities, and price requirements.

Layered Architecture: Separate Client/API layer and CLI/Command layer for better maintainability.

Detailed Logging: All API requests, responses, and errors are logged to trading.log.

Tech Stack
Language: Python 3.x

API Wrapper: python-binance

CLI Framework: Click

Configuration: python-dotenv

Installation & Setup
Clone the Repository:
git clone https://github.com/laharipandey/binance-trading-bot-task.git

Install Dependencies:
pip install -r requirements.txt

Configure Environment Variables:
Create a .env file and add your credentials:
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_secret_key

Usage Guide
Place a Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.01

Place a Limit Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.01 --price 80000

Project Structure
bot/client.py: Binance API connection logic.

bot/validators.py: Input validation logic.

bot/logging_config.py: Centralized logging setup.

cli.py: Main entry point for the CLI.
