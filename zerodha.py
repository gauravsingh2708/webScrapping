from selenium import webdriver
import time
import csv
import xlwt
from xlwt import Workbook

username='AI3416'
password="@1gmailco"
pin='918273'
url='https://kite.zerodha.com'

driver = webdriver.Chrome("/Users/gaurav/Downloads/chromedriver")
driver.get(url)
driver.find_element_by_id('userid').send_keys(username)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_class_name('actions').click()
time.sleep(2)
driver.find_element_by_id('pin').send_keys(pin)
driver.find_element_by_class_name('actions').click()
time.sleep(10)
driver.find_element_by_class_name('button-outline').click()
time.sleep(4)
data2=driver.find_element_by_class_name('market-depth').text
print(type(data2))
print(data2)
file=open('zerodha_data12.csv','w')
writer=csv.writer(file)
writer.writerow(['Nifty 50','sensex','BankBaroda(share price)','volume','LTT','Bid-1','orders-1','Qty-1','Bid-2','orders-2','Qty-2','Bid-3','orders-3','Qty-3','Bid-4','orders-4','Qty-4','Bid-5','orders-5','Qty-5','Total-1','offer-1','orders-1','Qty-1','offer-2','orders-2','Qty-2','offer-3','orders-3','Qty-3','offer-4','orders-4','Qty-4','offer-5','orders-5','Qty-5','Total-2','Average_price'])
while(1):
    data=driver.find_element_by_class_name('pinned-instruments').text
    data1=driver.find_element_by_class_name('instruments').text
    data2=driver.find_element_by_class_name('market-depth').text
    dataitem=[]
    dataItemFinal=[]
    datitemtoadd=[]
    num=''
    for i in data2:
        if(i.isdigit() or i=='.' or i==',' or i=='-' or i==':'):
            num+=i
            continue
        else:
            if(num=='' or num=='.'):
                continue
            dataitem.append(num)
            num=''
    for i in dataitem:
        if(i[0]=='.'):
            dataItemFinal.append(float(i[1:]))
            continue
        if(',' in i):
            i=i.replace(',','')
            dataItemFinal.append(float(i))
            continue
        if("-" in i or ':' in i):
            dataItemFinal.append(i)
            continue
        dataItemFinal.append(float(i))
    # print(dataItemFinal)
    datitemtoadd.append(data[9:17])
    datitemtoadd.append(data[32:40])
    datitemtoadd.append(0)
    datitemtoadd.append(dataItemFinal[37])
    datitemtoadd.append(dataItemFinal[41])
    datitemtoadd.extend(dataItemFinal[0:32])
    datitemtoadd.append(dataItemFinal[38])
    # print(datitemtoadd)
    writer.writerow(datitemtoadd)
    time.sleep(1)
    # print(data[9:17]+" "+data[32:40])
file.close()