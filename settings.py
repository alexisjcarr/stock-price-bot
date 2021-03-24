from decouple import config


API_KEY_ = config(API_KEY)

URL = "https://financialmodelingprep.com/api/v3/stock/real-time-price/EB?\
    apikey={}".format(API_KEY_)
