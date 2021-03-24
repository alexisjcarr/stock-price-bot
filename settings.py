import os


URL = "https://financialmodelingprep.com/api/v3/stock/real-time-price/EB?apikey={}".format(os.environ.get('API_KEY'))
