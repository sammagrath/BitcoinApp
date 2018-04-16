'''
Created on 16/04/2018

@author: sammagrath
'''
from bittrex.bittrex import Bittrex, API_V2_0

my_bittrex = Bittrex("f4627e90eca34bc586987fbd4fc9b5c9", "6bdb87dabb534212ad945a423d5eeec3",
                     api_version=API_V2_0)  # or defaulting to v1.1 as Bittrex(None, None)


# my_bittrex.get_markets()

# print(my_bittrex.get_currencies())

# retrieve and print current balance of VTC(Vertcoin) wallet to console
vtc = my_bittrex.get_balance("VTC")
print("VTC Wallet: \n")
print(vtc)
print()
# retrieve order for NEO using unique ID
my_order = my_bittrex.get_order("8026af9d-307c-4acb-bc03-7918ccdb7f3f \n")

#retrieve order date from order object
print("My Order: \n")
print(my_order, '\n')
my_order_date = my_order['result']['Closed']
print("Order close date: \n", my_order_date)

# retrieve value of order in BTC
print("Example of keys: \n")
keys = my_order.keys()
print(keys)
print()

#retrieve price value for order from dict
my_order_value = my_order['result']['Price']
print("Order value: ")
print(my_order_value, "BTC" + '\n')

#retrieve current fiat value of BTC
current_btc_summary = my_bittrex.get_market_summary("USDT-BTC")
print("Current BTC price:")
print(current_btc_summary['result']['Last'], "USD \n")
print(current_btc_summary)



