#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"



#Inputs for our variables  including the rate charged for commission by Berkshire Hathaway(3%), the price of each share when
#Lakshmi bought the shares ($900.00), the price of each share when Lakshmi sold her shares ($942.75) and the number of shares
#she bought/sold (2000).

#Expected output is that Lakshmi will lose $25065.00 by selling her shares.

commission = 0.03
buying_share_price = 900
selling_share_price = 942.75
share_number = 2000

#Displaying price of shares at time of purchase
print"Price of shares at time of purchase:", "$" +str(buying_share_price)

#Displaying the number of shares purchased
print"Number of shares purchased: ",share_number

#Displaying the cost of shares before commission by calculating cost of shares multiplied by buying share price
cost_of_shares = share_number*buying_share_price
print"Cost of purchasing shares before commission:","$" +str(cost_of_shares)

#Displaying the amount charged for commission at time of purchase
buying_commission_amount = cost_of_shares*commission
print"The amount of commission charged at time of purchase:", "$" +str(buying_commission_amount)

#Displaying total cost of purchase
total_cost = buying_commission_amount+cost_of_shares
print"The total cost of the purchasing transaction is:", "$" +str(total_cost)

#Displaying gross revenue from selling shares before subtracting commission
gross_revenue = selling_share_price*share_number
print"Revenue from selling shares before commission:", "$" +str(gross_revenue)

#Displaying commission charged at time of selling shares by multiplying the commision percentage times total
#money recieved from selling shares
selling_commission = gross_revenue*commission
print"Commission charged at time of selling shares:", "$" +str(selling_commission)

#Displaying net revenue of the sale of shares after commission by subtracting the commission charged at time of sale from revenue
#gained at time of sale.
net_revenue = gross_revenue-selling_commission
print"Revenue from selling shares after commission:", "$" +str(net_revenue)

#Displaying money gained/lost by subtracting total cost for purchasing shares  from revenue gained through selling shares
#after commission
profit = net_revenue-total_cost
print"Money gained/lost through selling shares:" " -$" +str(abs(profit))