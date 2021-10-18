import dotenv
import pandas as pd
from dotenv import load_dotenv
import typing
import os
import fmpsdk

load_dotenv()
apikey=os.environ.get('api-key')
print(apikey)

companies=[]
marketcap= 1000000000

screener = fmpsdk.stock_screener(apikey,market_cap_more_than=marketcap,beta_more_than=1,exchange='NASDAQ',limit=100,is_actively_trading=True)



