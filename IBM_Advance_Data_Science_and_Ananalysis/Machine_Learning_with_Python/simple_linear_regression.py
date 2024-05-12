import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
import requests

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/FuelConsumptionCo2.csv"
response = requests.get(url)

#if response.status_code == 200:
#    with open("FuelConsumptionCo2.csv", "wb") as f:
#        f.write(response.content)
#        print("File downloaded successfully!")
#else:
#    print("Failed to download the file. Status code:", response.status_code)


df = pd.read_csv('FuelConsumptionCo2.csv')
print(df.head(2))

cdf = df[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB','CO2EMISSIONS']]
print(cdf.head(3))

viz = cdf[['CYLINDERS','ENGINESIZE','CO2EMISSIONS','FUELCONSUMPTION_COMB']]
viz.hist()
plt.show()

plt.scatter(cdf.FUELCONSUMPTION_COMB, cdf.CO2EMISSIONS, color='blue')
plt.xlabel("FUELCONSUMPTION_COMB")
plt.ylabel("Emission")
plt.show()

plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS,  color='blue')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()

plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS,  color='blue')
plt.xlabel("CYLINDER")
plt.ylabel("Emission")
plt.show()