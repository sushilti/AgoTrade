import dotenv
from fmpsdk.company_valuation import financial_ratios
import pandas as pd
from dotenv import load_dotenv
import typing
import os
import fmpsdk

load_dotenv()
apikey=os.environ.get('api-key')
companies=[]
marketcap= 1000000000

screener = fmpsdk.stock_screener(apikey,market_cap_more_than=marketcap,beta_more_than=1,exchange='NASDAQ',limit=100,is_actively_trading=True)
#screener=fmpsdk.nasdaq_constituent(apikey)
print(screener)

for item in screener:
    companies.append(item['symbol'])


valueratios={}

#get finacial ratios
count=0
print(companies)
for company in companies:
    try:
        if count<100:
             count=count+1
             fin_ratio=fmpsdk.financial_ratios(apikey,symbol=company,period="annual",limit=20)
             
             valueratios[company]={}
             valueratios[company]['ROCE']=fin_ratio[0]['returnOnCapitalEmployed']
             valueratios[company]['PBRatio']=fin_ratio[0]['priceToBookRatio']
             #valueratios[company]["ROIC"]
    except:
        pass
        
print(valueratios)    




