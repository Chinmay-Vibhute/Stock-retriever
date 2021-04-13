from tda import auth, client
from tda.orders import EquityOrderBuilder, Duration, Session
import json
import config
import datetime

# limit order of 5 shares of netflix stock at 18 dollars a share
builder = EquityOrderBuilder('NFLX', 5)
builder.set_instruction(EquityOrderBuilder.Instruction.BUY)
builder.set_order_type(EquityOrderBuilder.OrderType.LIMIT)
builder.set_price(18)
builder.set_duration(Duration.GOOD_TILL_CANCEL)
builder.set_session(Session.NORMAL)

response = c.place_order(config.account_id, builder.build())



