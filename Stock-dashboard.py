# Imran Hussain 20-1-22
# This program plots charts to a localhost weboage using data taken from Yahoo Finance.

# charting components
import mplfinance as mpf
import yfinance as yf
import pandas as pd
from io import BytesIO
# web components
import tornado.ioloop
import tornado.web

# ticker/s to be charted
df = yf.Ticker("GOOG").history(period="9mo")

# Creating the chart
figdata = BytesIO()
mpf.plot(df, style="yahoo",type="candle", show_nontrading=False, mav = 100, savefig=figdata)

# Web/frontend section
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("dashboard.html")

class ImageHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header('Content-Type', 'image/png')
        self.write(figdata.getvalue())

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/img", ImageHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()