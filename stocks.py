from tda import auth, client
from tda.orders import EquityOrderBuilder, Duration, Session
import json
import config
import datetime

# authenticate
try:
    c = auth.client_from_token_file(config.token_path, config.api_key)
except FileNotFoundError:
    from selenium import webdriver
    with webdriver.Chrome(executable_path=config.chromedriver_path) as driver:
        c = auth.client_from_login_flow(
            driver, config.api_key, config.redirect_uri, config.token_path)

# get price history for a symbol
r = c.get_price_history('TSLA',
        period_type=client.Client.PriceHistory.PeriodType.YEAR,
        period=client.Client.PriceHistory.Period.TWENTY_YEARS,
        frequency_type=client.Client.PriceHistory.FrequencyType.DAILY,
        frequency=client.Client.PriceHistory.Frequency.DAILY)

print(json.dumps(r.json(), indent=4))

# get a stock quote
response = c.get_quote('TSLA')

print(response.json())

# get stock fundamental data
response = c.search_instruments(['TSLA', 'PLTR'], c.Instrument.Projection.FUNDAMENTAL)

print(json.dumps(response.json(), indent=4))
