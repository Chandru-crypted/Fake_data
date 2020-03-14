import random as random
import pandas as pd
class Generation_fake_data(): 
    def __init__(self): 
        self.pay, self.month = [], []
        self.items = ['Food', 'Phone Bill', 'Clothing', 'Entertaintment', 'Fuel', 'Health']
        self.months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        self.bigpay, self.bigcategory, self.bigmonth, self.bigunique_no  = [], [], [], []

    def payment_list(self):
        for pay_itr in range(0, 6):
            self.pay.append(random.randrange(1,10000))
        return (self.pay)

    def categories(self):
        random.shuffle(self.items)
        return(self.items)
    
    def onemonth(self, month_name):
        self.pay, self.category = self.payment_list(), self.categories()
        for month_name_itr in range(len(self.category)):
            self.month.append(str(month_name))
        return (self.pay, self.category, self.month)
    
    def oneperson(self, uniq_no):
        for monthname in self.months:
            self.pay, self.category, self.month = self.onemonth(monthname)
            self.bigpay.extend(self.pay)
            self.bigcategory.extend(self.category)
            self.bigmonth.extend(self.month)
            self.bigunique_no.extend([uniq_no]*len(self.category))
        data = {'Unique_no':self.bigunique_no, 'Month':self.bigmonth, 'Category':self.bigcategory, 'Payments':self.bigpay}
        df = pd.DataFrame(data)
        return df
    
