from bs4 import BeautifulSoup
import requests
import pandas as pd
### make soup
url = 'https://en.wikipedia.org/wiki/Golden_State_Warriors'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
target=soup.find('table',{'class':"wikitable"})


df=pd.read_html(str(target))
# convert list to dataframe
df=pd.DataFrame(df[0])
print(df)
df.to_csv('GSW-sc.csv',encoding='utf-8',index=False,header=False)
