# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 15:25:22 2020

@author: chand
"""

import random as random
import pandas as pd

def payment_list():
    pay = []
    for pay_tr in range(0, 6):
        pay.append(random.randrange(1,10000))
    return (pay)

def categories():
    items = ['Food', 'Phone Bill', 'Clothing', 'Entertaintment', 'Fuel', 'Health']
    random.shuffle(items)
    return(items)

def onemonth(month_name):
    pay = payment_list()
    category = categories()
    month = []
    for month_name_itr in range(len(category)):
        month.append(str(month_name))
    return (pay, category, month)

def oneperson(uniq_no):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    bigpay, bigcategory, bigmonth, bigunique_no  = [], [], [], []
    for monthname in months:
        pay, category, month = onemonth(monthname)
        bigpay.extend(pay)
        bigcategory.extend(category)
        bigmonth.extend(month)
        bigunique_no.extend([uniq_no]*len(category))
    data = {'Unique_no':bigunique_no, 'Month':bigmonth, 'Category':bigcategory, 'Payments':bigpay}
    df = pd.DataFrame(data)
    return df

df = oneperson(3)
print(df.head())
df = df [df['Category'] == 'Clothing']
# Now i need to encode and put into a list in a such a way that 
# like [ A, B, C, D, A, B]
print(df)
# so we will assume the threshold value to be 2000 
thresh = 2000
#creating a new column that will have value 1 when the payments is >er than thresh 
transiton_list = [True if x > thresh else False for x in df['Payments']]
df['Encode'] = transiton_list
# creating a transiton table from the trasniton list
# the number of rows = number of col = unique elements in the transition list 

noofrows = len(df['Encode'].unique())
noofcol = len(df['Encode'].unique())
nooftrans_T_T = 0
nooftrans_T_F = 0 
nooftrans_F_T = 0
nooftrans_F_F = 0 
for i in range(len(transiton_list) - 1):
    if transiton_list[i] == True and transiton_list[i + 1] == True :
        nooftrans_T_T += 1
    if transiton_list[i] == True and transiton_list[i + 1] == False :
        nooftrans_T_F += 1
    if transiton_list[i] == False and transiton_list[i + 1] == True :
        nooftrans_F_T += 1
    if transiton_list[i] == False and transiton_list[i + 1] == False :
        nooftrans_F_F += 1

# i am not going to keep the strings True ot Flase in the table that i am going to 
#  generate 
# calcaultaing the probabality for true 
# calculating the probability for False 
nooftrue = transiton_list.count(True)
nooffalse = transiton_list.count(False)

#first take the first row as true 
# take the second row as False

#         True  False 
# True 
# False 

print(nooftrans_T_T)
print(nooftrans_T_F)
print(nooftrans_F_T)
print(nooftrans_F_F)
