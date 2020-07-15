#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import time


# In[2]:


from selenium.webdriver.common.keys import Keys


# In[3]:


driver=webdriver.Firefox()
driver.get("https://www.rettyclubs.com/parity/tran")
time.sleep(8)


# In[4]:


login=driver.find_element_by_class_name("van-field__control")


# In[5]:


login.send_keys("enter phone number")
pasword=driver.find_elements_by_class_name("van-field__body")
password=pasword[1]
password=password.find_element_by_class_name("van-field__control")
password.click()
password.send_keys("enter password")
button=driver.find_element_by_class_name("button-btn")
button.click()


# In[6]:


time.sleep(14)
transation_id=[]
number=[] 
colour=[]
cnt=0
predict_cnt=0


# In[7]:


orders=driver.find_element_by_class_name("orders")
string_val=orders.text
total_list=string_val.split('\n')
total_list=total_list[6:]
    #split the total_list:
for tlst in total_list:
    if cnt==0:
        transation_id.append(int(tlst))
    elif cnt==2:
        number.append(int(tlst))
        if int(tlst)%2==0:
            colour.append(1)
        else:
            colour.append(0)
    cnt=cnt+1
    if cnt==3:
        cnt=0



while(1):
    orders=driver.find_element_by_class_name("orders")
    string_val=orders.text
    total_list=string_val.split('\n')
    total_list=total_list[6:]
    transation_id.append(int(total_list[0]))
    number.append(int(total_list[2]))
    if(int(total_list[2])%2==0):
        colour.append(1)
    else:
        colour.append(0)
    
    #prediction algoo
    for c in colour:
        if c==1:
            predict_cnt=predict_cnt+1
        else:
            predict_cnt=predict_cnt-1
    
    
    if predict_cnt>=0:
        predict_colour=1
        print("next predicted colour is red")
    else:
        predict_colour=0
        print("next predicted colour is green")
    #time.sleep(170)
    ## modified for time 
    res=111
    while(res > 10):
        timer=driver.find_element_by_class_name("time")
        times=timer.text
        times=times.split('\n')
        times.remove(":")
        s=[str(i) for i in times]
        res = int("".join(s))
    ##time ....
    time.sleep(20)
    orders=driver.find_element_by_class_name("orders")
    string_val=orders.text
    total_list=string_val.split('\n')
    total_list=total_list[6:]
    if int(total_list[2])%2==0:
        expected_colour=1
    else :
        expected_colour=0
    
    if(predict_colour==expected_colour):
        print("sucess")
        print(predict_cnt)
    else:
        print("failure")
        #print("1 ")
        print(predict_cnt)
        if predict_cnt >=0:
            predict_cnt-=(predict_cnt)*0.50
        else:
            predict_cnt+=(predict_cnt)*0.50
        #print("2")
        print(predict_cnt)

# In[ ]:




