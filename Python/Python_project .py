#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os
import matplotlib.pyplot as plt
from itertools import combinations
from collections import Counter


    


# In[ ]:


def prediction_by_product(all_data):
    product_group=all_data.groupby('Product')
    quantity_ordered=product_group.sum()['Quantity Ordered']
    products=[product for product,df in product_group]
    prices=all_data.groupby('Product').mean()['Price Each']
    plt.style.use('dark_background')
    fig,ax1=plt.subplots()
    ax2=ax1.twinx()
    ax1.bar(products,quantity_ordered,color='r')
    ax2.plot(products,prices,'b-')

    ax1.set_xlabel('Product Name')
    ax1.set_ylabel('Quantity Ordered', color='b')
    ax2.set_ylabel('Price ($)',color='b')
    ax1.set_xticklabels(products,rotation='vertical',size=8)
    plt.show()


# In[3]:


def most_saleable_product(all_data):
    product_group=all_data.groupby('Product')
    quantity_ordered=product_group.sum()['Quantity Ordered']
    products=[product for product,df in product_group]
    plt.style.use('dark_background')
    plt.bar(products, quantity_ordered)
    plt.ylabel('Quantity Ordered')
    plt.xlabel('Product')
    plt.xticks(products,rotation='vertical',size=8)
    plt.show()


# In[4]:


def city_sales_highest_product(all_data):
    results=all_data.groupby('City').sum()
    cities=[city for city,df in all_data.groupby('City')]
    plt.style.use('dark_background')
    plt.bar(cities,results['Sales'])
    plt.xticks(cities,rotation='vertical',size=8)
    plt.ylabel("Sales in USD($)")
    plt.xlabel("City Name")
    plt.show()
    return


# In[5]:


def best_month_stock(all_data):
    results=all_data.groupby('Month').sum()
    months=range(1,13)
    plt.style.use('dark_background')
    plt.bar(months,results['Sales'])
    plt.xticks(months)
    plt.ylabel("Sales in USD($)")
    plt.xlabel("Month number")
    plt.show()
    return


# In[6]:


def advertismnt_diaplay(all_data):
    hours=[hour for hour,df in all_data.groupby('Hour')]
    plt.style.use('dark_background')
    plt.plot(hours,all_data.groupby(['Hour']).count())
    plt.xticks(hours)
    plt.xlabel('Hour')
    plt.ylabel('Number of Orders')
    plt.grid()
    plt.show()


# In[ ]:


if __name__ == '__main__':
    files=[file for file in os.listdir('E:/Python/Sales_Data/')]
    all_months_data=pd.DataFrame()
    for file in files:
        df=pd.read_csv("E:/Python/Sales_Data/"+file)
        all_months_data=pd.concat([all_months_data,df])
    all_months_data.to_csv("ganpat.csv",index=False)
    Records=pd.read_csv("ganpat.csv")
    
    nan_df=Records[Records.isna().any(axis=1)]
    Records=Records.dropna(how='all')
    Records=Records[Records['Order Date'].str[0:2]!='Or']
    Records['Quantity Ordered']=pd.to_numeric(Records['Quantity Ordered'])
    Records['Price Each']=pd.to_numeric(Records['Price Each'])
    Records['Month']=Records['Order Date'].str[0:2]
    Records['Month']=Records['Month'].astype('int32')
    
    
    
    
    Records['Sales']=Records['Quantity Ordered']* Records['Price Each']
    
    
    
    def get_city(address):
        return address.split(',')[1]
    def get_state(address):
        return address.split(',')[2].split(' ')[1]
    Records['City']=Records['Purchase Address'].apply(lambda x: get_city(x)+ '(' +get_state(x) + ')')
    
   
    
    Records['Order Date']=pd.to_datetime(Records['Order Date'])
    Records['Hour']=Records['Order Date'].dt.hour
    Records['Minute']=Records['Order Date'].dt.minute
    
    
    
    i=1
    while(i==1):
        print("1.best month for stock sale")
        print("2.which  city is histest number of sale of stock product")
        print("3.what time should we display advertisments to maxmize likehood of custmor's buying product in stock")
        print("4.what product sold most")
        print("5.What we Predicate by this data")
        print("Enter your Choice which quries you want to know")
        choice=int(input())
        if(choice==1):
                    best_month_stock(Records)
        elif(choice==2):
                        city_sales_highest_product(Records)
        elif(choice==3):
                        advertismnt_diaplay(Records)
        
        elif(choice==4):
                        most_saleable_product(Records)  
        elif(choice==5):
                        prediction_by_product(Records)
        else:
                print("enter the vaild input")
    
    


# In[ ]:





# In[ ]:




