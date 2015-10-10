#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


"""
Inputs: none from user. Variables are predefined as follows: rate charged for commission by Berkshire Hathaway(3%),
the price of each share when Lakshmi bought the shares ($900.00), the price of each share when Lakshmi sold her shares
($942.75) and the number of shares she bought/sold (2000).

Expected output: Lakshmi will lose $25065.00 by selling her shares.
"""

commission = 0.03
buying_share_price = 900
selling_share_price = 942.75
share_number = 2000



print"Price of shares at time of purchase:", "$" +str(buying_share_price)
print"Number of shares purchased: ",share_number


cost_of_shares = share_number*buying_share_price
print"Cost of purchasing shares before commission:","$" +str(cost_of_shares)


buying_commission_amount = cost_of_shares*commission
print"The amount of commission charged at time of purchase:", "$" +str(buying_commission_amount)


total_cost = buying_commission_amount+cost_of_shares
print"The total cost of the purchasing transaction is:", "$" +str(total_cost)

print"Price of shares at time of sale:", "$" +str(selling_share_price)

gross_revenue = selling_share_price*share_number
print"Revenue from selling shares before commission:", "$" +str(gross_revenue)


selling_commission = gross_revenue*commission
print"Commission charged at time of selling shares:", "$" +str(selling_commission)


net_revenue = gross_revenue-selling_commission
print"Revenue from selling shares after commission:", "$" +str(net_revenue)


profit = net_revenue-total_cost
print"Money gained/lost through selling shares:" " -$" +str(abs(profit))


"""
Test case:

Price of shares at time of purchase: $900
Number of shares purchased:  2000
Cost of purchasing shares before commission: $1800000
The amount of commission charged at time of purchase: $54000.0
The total cost of the purchasing transaction is: $1854000.0
Price of shares at time of sale: $942.75
Revenue from selling shares before commission: $1885500.0
Commission charged at time of selling shares: $56565.0
Revenue from selling shares after commission: $1828935.0
Money gained/lost through selling shares: -$25065.0
"""