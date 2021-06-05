#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 21:10:40 2021

@author: narimanemadzadeh
"""


import numpy as np

"""Net Operating Income (NOI) most important number for rental properties. 
This is the amount of money you get after all expenses, 
except financing costs like principal and interest payments. A good rule of thumb
is to multiply the gross rent by 55%. Roughly 45% goes toward vacancies, insurance, 
property taxes, repairs, gardening/lawn care, property management and so on. """

purchased_price = input("How much did you purchase your investment property?")
user_purchased_price = int(purchased_price)

gross_rent = input("What is your expected gross rent per month?")
user_anual_gross_rent = int(gross_rent)*12

net_operating_income = user_anual_gross_rent * 0.55

capitalization_rate = net_operating_income / user_purchased_price

if capitalization_rate > 0.09:
    print("This is an excellent investment based on your cap rate at",capitalization_rate,"!")
elif capitalization_rate > 0.06:
    print("This is a good investment based on your cap rate at",capitalization_rate,".")
else:
    print("Your purchasing price is too high for your estimated rental. This investment\
          is not ideal because your capitlaization rate is:",capitalization_rate,".")
        