from tda import auth, client
from tda.orders import EquityOrderBuilder, Duration, Session
import json
import config
import datetime

# get option chain
response = c.get_option_chain('TSLA')

print(json.dumps(response.json(), indent=4))

# get all call options
response = c.get_option_chain('TSLA', contract_type=c.Options.ContractType.CALL)

print(json.dumps(response.json(), indent=4))

# get call options for a specific strike
response = c.get_option_chain('TSLA', contract_type=c.Options.ContractType.CALL, strike=300)

print(json.dumps(response.json(), indent=4))

# get call options for a specific strike and date range
start_date = datetime.datetime.strptime('2020-04-24', '%Y-%m-%d').date()
end_date = datetime.datetime.strptime('2020-05-01', '%Y-%m-%d').date()

response = c.get_option_chain('TSLA', contract_type=c.Options.ContractType.CALL, strike=300, strike_from_date=start_date, strike_to_date=end_date)

print(json.dumps(response.json(), indent=4))