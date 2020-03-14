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
    
def multiperson(num):
    m_df = pd.DataFrame(oneperson(0))
    print(m_df.head())
    for i in range(1, num+1):
        m_df = m_df.append(oneperson(i))
    return(m_df)

datframe = multiperson(10)
dataframe.to_csv(r'C:Users\ \File Name.csv', index = False)
