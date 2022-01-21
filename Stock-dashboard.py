# I Hussain 20-1-22
# This program plots charts to a localhost webpage using data taken from Yahoo Finance.
# Currently under development. Long term plan is to plot the stocks that I own, refreshing daily, and highlight the 100 day MA.

# Charting modules
import mplfinance as mpf
import yfinance as yf
from io import BytesIO
# Web modules
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