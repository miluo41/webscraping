# -*- coding: utf-8 -*-
"""
Extracting beta value of megacap companies on NYSE using BeautifulSoup. 
A total of 47 html pages were scaped.
complanylist_NY.csv file was downloaded from Nasdaq.com
@author: miluo
"""
import csv
import requests
from bs4 import BeautifulSoup
import numpy

with open('companylist_NY.csv','r') as csvfile:
    infile=csv.reader(csvfile)
    next(infile,None)
    company_dict={row[0]:[row[3],row[8]] for row in infile}
    
mega_cap={}    
for key in company_dict:
    if float(company_dict[key][0]) > 1E11:
        mega_cap[key]=company_dict[key]

def get_parameter(url,name='beta'):
    res=requests.get(url)
    soup=BeautifulSoup(res.text)
    a_tab=soup.find('a',id=name)
    return float(a_tab.parent.findNext('td').string)     

mega_cap_beta={}
for key in mega_cap:
    url=mega_cap[key][1]
    beta=get_parameter(url)
    mega_cap_beta[key]=beta
                 
print(numpy.mean(list(mega_cap_beta.values())))
#0.824, indicating less volitility

with open('company_beta.csv','w',newline='') as outfile:
    writer=csv.writer(outfile)
    writer.writerow(['symbol','beta'])
    for key,value in mega_cap_beta.items():
        writer.writerow([key, value])
        
    




    

