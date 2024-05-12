import requests
from bs4 import BeautifulSoup
import pandas as pd
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html'
html_data = requests.get(url).text
    
soup = BeautifulSoup(html_data, 'html.parser')
soup.find_all('title')
gme_revenue = pd.DataFrame(columns=['Date', 'Revenue'])

for row in soup.find('tbody').find_all ('tr'):
    col = row.find_all('td')
    date = col[0].text.strip()
    revenue = col[1].text.strip()
    new_row = pd.DataFrame({'Date': [date], 'Revenue': [revenue]})  # Create a DataFrame with new row data
    gme_revenue = pd.concat([gme_revenue, new_row], ignore_index=True)
import requests
from bs4 import BeautifulSoup
import pandas as pd
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html'
html_data = requests.get(url).text
    
soup = BeautifulSoup(html_data, 'html.parser')
soup.find_all('title')
gme_revenue = pd.DataFrame(columns=['Date', 'Revenue'])

for row in soup.find('tbody').find_all ('tr'):
    col = row.find_all('td')
    date = col[0].text.strip()
    revenue = col[1].text.strip()
    new_row = pd.DataFrame({'Date': [date], 'Revenue': [revenue]})  # Create a DataFrame with new row data
    gme_revenue = pd.concat([gme_revenue, new_row], ignore_index=True)
    
    
gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace(',|\$',"")

gme_revenue.dropna(inplace=True)
gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]

print(gme_revenue.tail())
    
gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace(',|\$',"")

gme_revenue.dropna(inplace=True)
gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]

print(gme_revenue.tail())