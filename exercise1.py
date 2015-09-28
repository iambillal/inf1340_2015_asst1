#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

#Input commission
#Input share_price
#Input share_number
#Calculate cost_of_shares as share_price multiplied by share_number
#Display cost_of_shares
#Calculate commission_amount as commission multiplied by cost_of_shares
#Display commission_amount
#Calculate total_cost as commission_amount plus cost_of_shares
#Display total_cost

#Calculate gross_revenue by multiplying selling_share_price and share_number
#Display gross_revenue
#Calculate selling_commission_amount by multiplying gross_revenue and commission
#Display selling_commission_amount
#Calculate net_revenue by subtracting selling_commission_amount from gross_revenue
#Display net_revenue
#Calculate profit by subtracting total_cost from net_revenue


money = 2000.00
print(money)

commission = 0.03
buying_share_price = 900
selling_share_price = 942.75
share_number = 2000

cost_of_shares = share_number*buying_share_price
print(cost_of_shares)

buying_commission_amount = cost_of_shares*commission
print(buying_commission_amount)

total_cost = buying_commission_amount+cost_of_shares
print"The total cost is: ", total_cost

gross_revenue = selling_share_price*share_number
print(gross_revenue)

selling_commission = gross_revenue*commission
print(selling_commission)

net_revenue = gross_revenue-selling_commission
print(net_revenue)

profit = net_revenue-total_cost
print(profit)