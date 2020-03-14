"Necessary funcitons, use multiperson() takes the number of people that u want to generate the data" 

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

def oneperson(uniq_no, year):
    months = [1,2,3,4,5,6,7,8,9,10,11,12]
    bigpay, bigcategory, bigmonth, bigunique_no, bigyear  = [], [], [], [], []
    for monthname in months:
        pay, category, month = onemonth(monthname)
        bigpay.extend(pay)
        bigcategory.extend(category)
        bigmonth.extend(month)
        bigunique_no.extend([uniq_no]*len(category))
        bigyear.extend([year]*len(category))
    data = {'Unique_no':bigunique_no,'Year':bigyear, 'Month':bigmonth, 'Category':bigcategory, 'Payments':bigpay}
    df = pd.DataFrame(data)
    return df
oneperson(2, 2015)

def multiyear(year, num):
    m_df = pd.DataFrame(oneperson(0, year))
    for i in range(1, num):
        year = year + 1
        m_df = m_df.append(oneperson(i, year))
    return(m_df)
