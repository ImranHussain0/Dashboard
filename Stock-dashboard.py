# Imran Hussain 20-1-22
# This program plots charts using data taken from Yahoo Finance.

import mplfinance as mpf
import yfinance as yf
import pandas as pd

df = yf.Ticker("AMZN").history(period="9mo")

# code to plot moving average 100
mpf.plot(df, style="yahoo",type="candle", show_nontrading=False, mav = 100)

# Advanced way to plot moving averge 100. Can be modified for custom indicators.
# df["100ma"] = df["Open"].rolling(window=100).mean()
# movingave = [ mpf.make_addplot(df["100ma"])]
# mpf.plot(df, type="candle", addplot = movingave)