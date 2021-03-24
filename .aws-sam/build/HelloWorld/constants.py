from decouple import config


URL = f"https://financialmodelingprep.com/api/v3/stock/real-time-price/EB?\
    apikey={config(API_KEY)}"
