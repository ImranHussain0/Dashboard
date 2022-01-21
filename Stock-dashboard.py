# Imran Hussain 20-1-22
# This program plots charts to a localhost weboage using data taken from Yahoo Finance.

# charting components
import mplfinance as mpf
import yfinance as yf
import pandas as pd
import base64
from io import BytesIO
# web components
import tornado.ioloop
import tornado.web

# ticker/s to be charted
df = yf.Ticker("MSFT").history(period="9mo")

figdata = BytesIO()
mpf.plot(df, style="yahoo",type="candle", show_nontrading=False, mav = 100, savefig=figdata)

# Advanced way to plot moving averge 100. Can be modified for custom indicators.
# df["100ma"] = df["Open"].rolling(window=100).mean()
# movingave = [ mpf.make_addplot(df["100ma"])]
# mpf.plot(df, type="candle", addplot = movingave)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        #self.write("Test text")
        self.set_header('Content-Type', 'image/png')
        self.write(figdata.getvalue())

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()